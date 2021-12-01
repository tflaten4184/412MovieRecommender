# Author: Tyler
# Purpose: Preprocessing the CSV and saving the result.

import pandas as pd
import numpy as np
from remove_columns import trim_columns
from remove_punctuation import remove_symbols
from remove_stop_words import remove_stopwords
from stemming import apply_stemming


# Load csv
infileName = "netflix_titles.csv"
with open(infileName) as infile:

    original_df = pd.read_csv(infileName)
    print(original_df)
    # remove unnecessary columns
    trimmed_df = trim_columns(original_df) 


    # Perform the following operations: (order?)
    # remove symbols
    trimmed_df["description"] = trimmed_df["description"].apply(remove_symbols)
    print(trimmed_df)

    trimmed_df.to_csv("netflix-dirty.csv")

    # remove stop words
    trimmed_df["description"] = trimmed_df["description"].apply(remove_stopwords)
    print(trimmed_df)

    # stemming conversion
    trimmed_df["description"] = trimmed_df["description"].apply(apply_stemming)
    print(trimmed_df)

    # movie titles to array
    titlesArr = trimmed_df["title"].to_numpy()
    print(titlesArr)

    trimmed_df.to_csv("netflix-cleaned.csv")

