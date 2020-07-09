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
BIRTHPERIOD = 1900

# Note that these have been pre-set here to reduce the runtime - update if the 
# data changes. Elizabeth Barret Browning has been removed from the list due to
# the tenuous link.
SLAVEOWNERWIKIDATA = ['Q3523736', 'Q160852', 'Q7347686']

df = pd.read_csv(FILENAME)
df.dropna(subset = ['en_wikipedia_url'], inplace = True)

# Trigger words - see trigger_words_investigation.ipynb
trigger_words = {'slave':20,
                 'slaves':20,
                 'slavery':10,
                 'owned':5,
                 'land':5,
                 'treatment':5,
                 'plantation':15,
                 'actor':-20,
                 'poet':-20,
                 'writter':-20,
                 'author':-20,
                 'composer':-20,
                 'abolitionists':-20,
                 'abolitionist':-20,
                 'anti-slavery':-30,
                 'anti-salavery society':-20,
                }

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
            score -= 50
        
        # Filter out those whose ethnicity is bame
        if row['ethnicity'] == 'bame':
            score -= 50
        
        # Reduce the score if the date of birth is outside the range
        try: # Not all entries have a date of birth
            if int(row['born_in']) > BIRTHPERIOD:
                score -= 20
        except:
            pass
            
        # Increase the score of the know slave owners from wikidata
        if row['wikidata_id'] in SLAVEOWNERWIKIDATA:
            score += 50
        
        # Increase the score of the know slaves from the wiki list
        if name in slave_owners_wiki:
            score += 50
            
        print(score, row['full_name'])
        scores[row['full_name']] = score
    
    return scores

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
    
    file = open('bad_actor_scores_combined_altered.txt', 'w', encoding = 'utf8')
    file.write(str(sorted_scores)) 
    file.close()