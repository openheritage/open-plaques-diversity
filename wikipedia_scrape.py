import wikipedia
import pandas as pd

FILENAME = 'open-plaques-subjects-london.csv'
df = pd.read_csv(FILENAME)

df.dropna(subset = ['en_wikipedia_url'], inplace = True)

# Trigger words and there weightings


for index, row in df.iterrows():
    name = row['en_wikipedia_url'].split('/')[-1]
    contents = wikipedia.page(name).content
    