from wikipedia_scrape import get_wiki_contents
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from collections import Counter

import re
import pandas as pd

FILENAME = 'open-plaques-subjects-london.csv'
ABOLITLIST = 'https://en.wikipedia.org/wiki/List_of_abolitionists'
SLAVEOWNERSURL = ['https://en.wikipedia.org/wiki/List_of_slave_owners',
                  'https://en.wikipedia.org/wiki/Category:British_slave_owners']

df = pd.read_csv(FILENAME)

df.dropna(subset = ['en_wikipedia_url'], inplace = True)

# Trigger words - see trigger_words_investigation.ipynb
trigger_words = {'slave':10,
                 'slaves':10,
                 'slavery':10,
                 'owned':5,
                 'treatment':5,
                 'refused':3,
                 'plantation':15}

def get_scores():
    # Get a list of abolitionists from the wiki list
    ab_list = get_wiki_contents(ABOLITLIST).lower()
    
    # Get a list of the know slave owners from wiki
    slave_owners_wiki = get_wiki_contents(SLAVEOWNERSURL[0]).lower() + \
        get_wiki_contents(SLAVEOWNERSURL[1]).lower()
        
    scores = {}
    for index, row in df.iterrows(): 
        name = row['full_name']
        
        # Make an initial score using word appearances in the corresponding wikipages
        score = trigger_word_score(row['en_wikipedia_url'])
        
        # Filter out those which are abolitionisits 
        if name in ab_list:
            score = 0
        
        # Filter out those whose ethnicity is bame
        if row['ethnicity'] == 'bame':
            score = 0
        
        # Increase the score of the know slaves from the wiki list
        if name in slave_owners_wiki:
            score += 50
            
        print(score, row['full_name'])
        scores[row['full_name']] = score 

def trigger_word_score(url):
    content = get_wiki_contents(url).lower()
    
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(content) 

    filtered_sentences = [w for w in word_tokens if not w in stop_words] 

    # Filter out the punctuation
    nonPunct = re.compile('.*[A-Za-z].*')  # must contain a letter
    filtered = [w for w in filtered_sentences if nonPunct.match(w)]
    counts = Counter(filtered)
    
    score = 0
    words = counts.keys()
    for trigger_word in trigger_words:
        if trigger_word in words:
            score += trigger_words[trigger_word]
    
    return score
    
if __name__ == '__main__':
    scores = get_scores()
    print(scores)
    sorted_scores = sorted(scores.items(), key=lambda item: item[1])[::-1]
    
    print(sorted_scores[:200])
    
    file = open('bad_actor_scores_sorted.txt', 'w', encoding = 'utf8')
    file.write(str(sorted_scores)) 
    file.close()