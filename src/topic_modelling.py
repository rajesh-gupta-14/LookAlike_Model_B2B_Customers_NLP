#==========================================
# Title: Topic modelling using LDA
# Author: Rajesh Gupta
# Date:   1 Mar 2019
#==========================================
import logging
from datetime import datetime
import csv, json
import os, string
import pandas as pd, numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from utility_functions import *
from global_vars import *

def preprocessing(data):
    try:
        # Remove punctuations
        data = [_char for _char in data if _char not in string.punctuation]
        # Changing back to text
        data = "".join(data)
        # Tokenize
        data = data.split()
    except Exception:
        data = [str(0)]
    return data

feature_set = unpickle("SIZE", "feature_sets")
#feature_set["SIZE"] = feature_set["SIZE"].apply(preprocessing)
cv = CountVectorizer(analyzer=preprocessing, max_df = 1.0, min_df = 2)
vector_data = cv.fit_transform(feature_set["SIZE"])
#print(feature_set["S"])
#print(vector_data)
#print(type(vector_data))
lda_model = LatentDirichletAllocation(n_topics=10, max_iter=1000, learning_method='online')
model = lda_model.fit(vector_data)
print(model)
lda_z = model.transform(vector_data)
#feature_set["new"] = [for list(lda_z]
feature_set["new"] = list(lda_z)
print(feature_set["new"])
#feature_set["S"] = ""
##feature_set["T"] = ""
#feature_set["U"] = ""

#feature_set[["S","T","U"]] =  lda_z
#print(feature_set[["S","T","U"]])


def print_topics(model, vectorizer, top_n=20):
    for idx, topic in enumerate(model.components_):
        print("Topic %d:" % (idx))
        print([(vectorizer.get_feature_names()[i], topic[i])
                        for i in topic.argsort()[:-top_n - 1:-1]])
 
#print("LDA Model:")
#print_topics(lda_model, cv)
#print("=" * 20)