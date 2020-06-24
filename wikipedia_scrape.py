import wikipedia
import pandas as pd

FILENAME = 'open-plaques-subjects-london.csv'
df = pd.read_csv(FILENAME)

df.dropna(subset = ['en_wikipedia_url'], inplace = True)

# Trigger words and there weightings

def main():
    for index, row in df.iterrows():
        r = row['en_wikipedia_url']
        
def get_wiki_contents(url):
    try:
        name = url.split('/')[-1]
        contents = wikipedia.page(name).content
    except:
        print('Wiki retrieval failed')
    return contents    
    
if __name__ == '__main__':
    main()