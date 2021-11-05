#Project for SE412  Fall 2021
#Jacob

import pandas as pd
from nltk.corpus import stopwords

pd.read_csv("netflix_titles_nov_2019.csv", encoding="utf-8") 

file = pd.read_csv("netflix_titles_nov_2019.csv") 

file.columns = ['show_id', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description', 'type']
file['description'] = file['description'].str.lower().str.split()  

stop = stopwords.words('english')

file['Title'] = file['Title'].apply(lambda x: [item for item in x if item not in stop])
file['Body'] = file['Body'].apply(lambda x: [item for item in x if item not in stop])

file.to_csv("netflix_titles_nov_2019_removed_stop.csv")