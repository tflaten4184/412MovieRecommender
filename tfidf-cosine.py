# This file is used for generating recommendations usign cosine similiarity

import pandas as pd
import numpy as np
import os
import sys
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

# Returns list of all titles from dataset
def get_all_titles():
    titles = []  # list of all titles
    with open(os.path.join(sys.path[0], "netflix-cleaned.csv"), encoding="utf8") as inFile:
        df = pd.read_csv(inFile, encoding="utf8")
        for index, row in df.iterrows():
            titles.append(row['title'])

    return titles

# This function gets 10 recommendations.
# Input: movie title as a string
# Output: returns a list of tuples, of the form: (title, similarity)
#    (sorted by descending similarity)
def recommend(movie: str, filename: str):
    try:
        infileName = filename
        corpus = [] # list of all descriptions
        with open(os.path.join(sys.path[0], infileName), encoding="utf8") as inFile:
            df = pd.read_csv(inFile, encoding="utf8")
            # print("DF = ")
            # print(df)
            for index, row in df.iterrows(): #add description to corpus
                corpus.append(row['description'])
            # print("CORPUS = ")
            # print(corpus)
    except:
        print("\nCant find file! Try again!\n")
        return None

    try:
        current_index = int(df.loc[df['title'] == movie]['index'])
    except TypeError:
        return -1

    # print("Current Index: ", current_index)

    # tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english') 
    tf = TfidfVectorizer() 
    tfidf_matrix =  tf.fit_transform(corpus) #vectorize
    # results = tf.get_feature_names_out()

    cs_matrix = cosine_similarity(tfidf_matrix[current_index], tfidf_matrix[0:]) #compare first description with first 10 documents
    # print("length cs_matrix = ", len(cs_matrix[0]))
    # print("length df = ", len(df))
    df['similarity'] = cs_matrix[0]
    # print(df)

    # Might not need to save to file?
    # np.savetxt("output.txt", cs_matrix, fmt='%s') #output np array to file
    #print(cs_matrix)

    # Get top 10 results, sorted by descending similarity
    results = df.sort_values(by=['similarity'], ascending=False)[['title', 'similarity']].head(11)
    results_tuples = list(results.to_records(index=False))
    # Returns a list of 10 tuples of the form: (title, similarity)
    return results_tuples

if __name__ == "__main__":

    print("Testing Cases:")
    print("Recommend for 'Kota Factory'", "netflix-cleaned.csv")
    print(recommend("Kota Factory", "netflix-cleaned.csv"))
    print("Recommend for 'Zubaan'", "netflix-cleaned.csv")
    print(recommend("Zubaan", "sit.csv"))
