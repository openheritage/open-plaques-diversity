# Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import time
from qwikidata.sparql import (get_subclasses_of_item,
                              return_sparql_query_results)

# Set the filename of the csv for analysis - same directory
FILENAME = 'open-plaques-subjects-london.csv'
df = pd.read_csv(FILENAME)

# Remove the columns which don't have wikidata id's attached
df.dropna(subset = ['wikidata_id'], inplace = True)

# Store the results in a list
results = []
print('Total wikidata examples {0}'.format(df.shape[0]))

# Iterate throught the wiki IDs
for i, row in df.iterrows():
    
    # Waiting will mean more of the queries come back with results
    time.sleep(1)
    
    # P172 represents the ethnicity
    sparql_query = """
    SELECT ?item ?itemLabel 
    WHERE 
    {
      wd:""" + row['wikidata_id'] + """ wdt:P172 ?item.
      SERVICE wikibase:label {bd:serviceParam wikibase:language "en" . }
    }
    """
    
    # Use a try to avoid errors where the property field for cizenship isn't present e.g. objects
    try:
        res = return_sparql_query_results(sparql_query)
        results.append(res['results']['bindings'][0]['itemLabel']['value'])
        print(i, end = ',')
    except:
        continue

# Condense the list into a frequency dictionary
res_dict = {}
for citizen in results:
    try:
        res_dict[citizen] += 1
    except:
        res_dict[citizen] = 1

y_pos = list(range(len(res_dict)))
plt.rcParams["figure.figsize"] = (16,9)
fig = plt.figure()
plt.barh(y_pos, res_dict.values())
plt.yticks(y_pos, res_dict.keys())

fig.suptitle('Ethnic group of plaques in London',  fontsize = 20)
plt.xlabel('Frequency', fontsize = 15)
plt.ylabel('Ethnic group',  fontsize = 15)

plt.show()
fig.savefig('Ethnic group horizontal bar chart')