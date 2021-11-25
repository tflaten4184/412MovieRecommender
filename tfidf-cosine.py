import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

infileName = "netflix-cleaned.csv"
corpus = []
with open(infileName) as inFile:
    df = pd.read_csv(inFile)
    for index, row in df.iterrows(): #add description to corpus
        corpus.append(row['description'])

# tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english') 
tf = TfidfVectorizer() 
tfidf_matrix =  tf.fit_transform(corpus) #vectorize
# results = tf.get_feature_names_out()
cs_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[0:10]) #compare first description with first 10 documents
np.savetxt("output.txt", cs_matrix, fmt='%s') #output np array to file 
print(cs_matrix)