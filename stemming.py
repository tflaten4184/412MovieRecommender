# Project for SE512  Fall 2021
# Author: PCourt Will D
# Purpose: Applies stemming to a string

from nltk.stem.porter import PorterStemmer
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Internal path for accessing data in netflix_titles_nov_2019
# files downloaded and stored in SE 512 folder of my computer.

# The following block only executes if the script is run directly
if __name__ == "__main__":
    ShowInfo = pd.read_csv("netflix_titles.csv")
    print(ShowInfo.shape)

    # Establishes a data frame to modify.
    PrimaryShowInfo = pd.DataFrame(ShowInfo)

    # Discards data columns that will not be used.
    PrimaryShowInfo = PrimaryShowInfo.drop(['show_id', 'director', 'cast', 'country',
                                        'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'type'], axis=1)


    def stemming(data):
        stemmer = PorterStemmer()
        tokens = word_tokenize(str(data))
        new_text = ""
        for w in tokens:
            new_text = new_text + " " + stemmer.stem(w)
            df = pd.DataFrame([x.split(';') for x in new_text.split(' ')])
        return df


    print(PrimaryShowInfo['description'])
    stemed_data = stemming(PrimaryShowInfo['description'])
    print(stemed_data)
    # stemming: process of reducing inflection in words to their root forms
    # - Stems are created by removing the suffixes or prefixes used with a word.

##############################################################################
# Use the original code (above) to implement the function and test case (below)
##############################################################################

# Input: any string
# Output: string after stemming
def apply_stemming(description: str) -> str:

    print("Not implemented")

    return description

# Test case:
# (Only executes if this script is run directly)
if __name__ == "__main__":
    test_string = "jumping runner eats"

    test_result = apply_stemming(test_string)

    print("Stemming applied:", test_result)