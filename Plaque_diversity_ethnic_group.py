# Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import time
from qwikidata.sparql import (get_subclasses_of_item,
                              return_sparql_query_results)

def get_ethnicity(filename):
    # Set the filename of the csv for analysis - same directory
    df = pd.read_csv(filename)
    
    # Remove the columns which don't have wikidata id's attached
    df.dropna(subset = ['wikidata_id'], inplace = True)
    
    # Store the results in a list
    results = []
    print('Total wikidata examples {0}'.format(df.shape[0]))
    
    # Iterate throught the wiki IDs
    for i, row in df.iterrows():
        
        # Waiting will mean more of the queries come back with results
        time.sleep(1)
        
        res = q_wikidata(row['wikidata_id'])
        
        if not res == None:
            results.append(res)
            print(i, end = ',')
            print(row['wikidata_id'])
    
    return results

def q_wikidata(wiki_id):
    # P172 represents the ethnicity
    sparql_query = """
    SELECT ?item ?itemLabel 
    WHERE 
    {
      wd:""" + wiki_id + """ wdt:P172 ?item.
      SERVICE wikibase:label {bd:serviceParam wikibase:language "en" . }
    }
    """
    
    # Use a try to avoid errors where the property field for cizenship isn't 
    # present e.g. objects
    try:
        res_all = return_sparql_query_results(sparql_query)
        return res_all['results']['bindings'][0]['itemLabel']['value']
    except:
        return None
        
        
def plot(results):
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
    
if __name__ == '__main__':
    results = get_ethnicity('open-plaques-subjects-london.csv')
    plot(results)