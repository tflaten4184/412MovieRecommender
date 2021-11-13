#Project for SE412  Fall 2021
# Author: Jacob
# Purpose: Removes stopwords from a string

import pandas as pd
from nltk.corpus import stopwords

# The following block only executes if the script is run directly
if __name__ == "__main__":
    pd.read_csv("netflix_titles.csv", encoding="utf-8") 

    file = pd.read_csv("netflix_titles_nov_2019.csv") 

    file.columns = ['show_id', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description', 'type']
    file['description'] = file['description'].str.lower().str.split()  

    stop = stopwords.words('english')

    file['Title'] = file['Title'].apply(lambda x: [item for item in x if item not in stop])
    file['Body'] = file['Body'].apply(lambda x: [item for item in x if item not in stop])

    file.to_csv("netflix_titles_nov_2019_removed_stop.csv")

##############################################################################
# Use the original code (above) to implement the function and test case (below)
##############################################################################

# Input: string
# Output: return string (stopwords removed)
def remove_stopwords(description: str) -> str:

    print("Not implemented")

    return description

# Test case:
# (Only executes if this script is run directly)
if __name__ == "__main__":

    test_string = "This is a string that contains some stop words."

    test_result = remove_stopwords(test_string)

    print("Stopwords removed:", test_result)