#Project for SE512  Fall 2021
#PCourt

import pandas as pd
from IPython.display import display


## Internal path for accessing data in netflix_titles_nov_2019
# files downloaded and stored in SE 512 folder of my computer.

ShowInfo = pd.read_csv(r"C:\Users\court\Google Drive\SCSU\SE 512\Project\netflix_titles_nov_2019.csv")

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