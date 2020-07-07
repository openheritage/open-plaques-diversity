from wikipedia_scrape import get_wiki_contents
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from collections import Counter

import re
import pandas as pd

FILENAME = 'open-plaques-subjects-london.csv'
df = pd.read_csv(FILENAME)

df.dropna(subset = ['en_wikipedia_url'], inplace = True)

abolistionist_words =  {'abolitionists':10,
                        'abolitionist':10,
                        'anti-slavery':10,
                        'campaign':5,
                        'Anti-Slavery Society':5,
                       }

scores = {}
for index, row in df.iterrows():
    url = row['en_wikipedia_url']
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
    for trigger_word in abolistionist_words:
        if trigger_word in words:
            score += abolistionist_words[trigger_word]
    
    print(score, row['full_name'])
    scores[row['full_name']] = score 
    
print(scores)
sorted_scores = sorted(scores.items(), key=lambda item: item[1])[::-1]

print(sorted_scores[:200])

file = open('abolitionists_scores_sorted.txt', 'w', encoding = 'utf8')
file.write(str(sorted_scores)) 
file.close()