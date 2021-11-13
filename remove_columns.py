#Project for SE512  Fall 2021
# Author: PCourt
# Purpose: Remove columns of a dataframe other than Title and Description

import pandas as pd
from IPython.display import display

## Internal path for accessing data in netflix_titles_nov_2019
# files downloaded and stored in SE 512 folder of my computer.

# The following block only executes if the script is run directly
if __name__ == "__main__":
    ShowInfo = pd.read_csv(r"netflix_titles.csv")

    #Number of data rows total.
    n = ShowInfo.shape[0]

    #Number of columns of data.
    d = ShowInfo.shape[1]

    print ('Rows = ', n, 'Columns = ', d)

    #Displays the first few rows of the data frame.
    display(ShowInfo.head())

    #Establishes a data frame to modify.
    PrimaryShowInfo = pd.DataFrame(ShowInfo)

    #Discards data columns that will not be used.
    PrimaryShowInfo = PrimaryShowInfo.drop(['show_id', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'type'], axis = 1)

    #Number of data rows total.
    n = PrimaryShowInfo.shape[0]

    #number of columns of data in the modified set.
    d = PrimaryShowInfo.shape[1]

    print ('Rows = ', n, 'Columns = ', d)

    #Displays the first few rows of the modified data frame.
    display(PrimaryShowInfo.head())

##############################################################################
# Use the original code (above) to implement the function and test case (below)
##############################################################################

# Input: pandas dataframe
# Output: pandas dataframe (columns removed)
def trim_columns(orig_df: pd.DataFrame) -> pd.DataFrame:

    result_df = orig_df
    print("Not Implemented")

    return result_df


# Test case:
# (Only executes if this script is run directly)
if __name__ == "__main__":

    test_df = pd.read_csv(r"netflix_titles.csv")

    result_df = trim_columns(test_df)

    print("Result with 2 columns:")
    print(result_df)