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
    name = url.split('/')[-1].replace('-','_')
    try:
        contents = wikipedia.page(name).content
        return contents 
    except:
        print('Wiki retrieval failed {0}'.format(name))
        return ''
    
if __name__ == '__main__':
    main()