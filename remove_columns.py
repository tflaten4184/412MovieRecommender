#Project for SE512  Fall 2021
# Author: PCourt
# Purpose: Remove columns of a dataframe other than Title and Description

import pandas as pd
from IPython.display import display

## Internal path for accessing data in netflix_titles_nov_2020
# files downloaded and stored in SE 512 folder of my computer.

##################################################################################
# Function to decrease the columns in the CSV file to just Title and Description.
##################################################################################

def trim_columns(orig_df: pd.DataFrame) -> pd.DataFrame:

    #Establishes a data frame to modify.
    result_df = pd.DataFrame(orig_df)

    #Discards data columns that will not be used.
    result_df = orig_df.drop(['show_id', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'type'], axis = 1)

    return result_df


# Test case:
# (Only executes if this script is run directly)
if __name__ == "__main__":

    test_df = pd.read_csv(r"netflix_titles.csv")

    result_df = trim_columns(test_df)

    print("Result with 2 columns:")
    print(result_df)