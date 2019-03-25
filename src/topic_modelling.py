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
    return data.split()

def topic_model():  
    logging.info("="*15 + "Unpickling of __feature__" + "="*15)  
    feature_set = unpickle("ACQUISITIONS", "feature_sets")
    #feature_set["SIZE"] = feature_set["SIZE"].apply(preprocessing)

    logging.info("="*15 + "Count vectorizer model being built" + "="*15)
    cv = CountVectorizer(analyzer=preprocessing, max_df = 1.0, min_df = 2)
    vector_data = cv.fit_transform(feature_set["ACQUISITIONS"])

    logging.info("="*15 + "LDA model being built" + "="*15)
    lda_model = LatentDirichletAllocation(n_topics=10, max_iter=1000, learning_method='online')
    model = lda_model.fit(vector_data)

    pickle(model, "lda_model", "topic_models")
    logging.info("="*15 + "LDA model saved" + "="*15)

    logging.info("="*15 + "Transforming feature data to get topic distribution vectors" + "="*15)
    lda_z = model.transform(vector_data)
    feature_set["TOPIC MODELLING DIST"] = list(lda_z)

    logging.info("="*15 + "Pickling the topic dist model for __feature__" + "="*15)
    pickle(feature_set, "test_acq", "transformed_feature_sets")
    print(feature_set[["TOPIC MODELLING DIST","COMPANY"]])
    
def make_data():
    logging.info("="*15 + "Unpickling of __topic_model_feature__" + "="*15)
    data = unpickle("test_acq", "extras")
    companies = list(data["COMPANY"].unique())
    final_data = pd.DataFrame()
    for company in companies:
        logging.info("="*15 + f"{company} dataset being calculated" + "="*15)
        company_data_dist = data[data["COMPANY"]==company][["TOPIC MODELLING DIST","COMPANY"]]
        comp_topic_vector = np.mean(company_data_dist["TOPIC MODELLING DIST"])
        company_df = pd.DataFrame([[comp_topic_vector,company]], columns=["TOPIC_MODEL_VECTOR","COMPANY"])
        final_data = pd.concat([final_data, company_df], axis=0, ignore_index=True)
        logging.info("="*15 + f"{company} dataset obtained" + "="*15)
    print(final_data)

def main():
    if TOPIC_MODELLING:
        logging.info("="*15 + "Topic modelling activated" + "="*15)
        topic_model()
    if MAKE_DATASETS:
        logging.info("="*15 + "Building datasets" + "="*15)
        make_data()


# ------------------------------
if __name__ == "__main__":
    configure_logger()
    main()
    # ------------------------------
    """
    def print_topics(model, vectorizer, top_n=3):
        for idx, topic in enumerate(model.components_):
            print("Topic %d:" % (idx))
            print([(vectorizer.get_feature_names()[i], topic[i])
                            for i in topic.argsort()[:-top_n - 1:-1]])
    
    print("LDA Model:")
    print_topics(lda_model, cv)
    print("=" * 20)
    """
    # ------------------------------
    
    
