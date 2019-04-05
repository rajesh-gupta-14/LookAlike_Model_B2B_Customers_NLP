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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def preprocessing(data):
    return data.split()

def topic_model(feature):
    logging.info("="*15 + f"Unpickling of {feature}" + "="*15)  
    feature_set = unpickle(feature, "feature_sets")
    #feature_set["SIZE"] = feature_set["SIZE"].apply(preprocessing)

    logging.info("="*15 + "Count vectorizer model being built" + "="*15)
    cv = CountVectorizer(analyzer=preprocessing, max_df = 1.0, min_df = 2)
    vector_data = cv.fit_transform(feature_set[feature])

    logging.info("="*15 + "LDA model being built" + "="*15)
    lda_model = LatentDirichletAllocation(n_topics=NO_OF_TOPICS, max_iter=NO_OF_ITERATIONS, learning_method='online')
    model = lda_model.fit(vector_data)

    pickle(model, f"lda_model_{feature}", "topic_models")
    logging.info("="*15 + "LDA model saved" + "="*15)

    logging.info("="*15 + "Transforming feature data to get topic distribution vectors" + "="*15)
    lda_z = model.transform(vector_data)
    feature_set["TOPIC_MODEL_VECTOR"] = list(lda_z)

    logging.info("="*15 + f"Pickling the topic dist model for {feature}" + "="*15)
    pickle(feature_set, f"test_{feature}", "transformed_feature_sets")
    print(feature_set[["TOPIC_MODEL_VECTOR","COMPANY"]])
    
def knn(df, feature):
	"""
	X_train, X_test, y_train, y_test = train_test_split(input,
								inputlabel, test_size=0.5)
	"""
	result = pd.DataFrame()
	for company in COMPANIES:
		logging.info("="*15 + f"kNN model for similar company to {company} being built" + "="*15)
		X_train = np.array(df[df["COMPANY"]!=company]["TOPIC_MODEL_VECTOR"].values.tolist())
		y_train = df[df["COMPANY"]!=company]["COMPANY"]
		logging.info("="*15 + f"kNN model - Train data READY" + "="*15)
		X_test = np.array(df[df["COMPANY"]==company]["TOPIC_MODEL_VECTOR"].values.tolist())
		y_test = df[df["COMPANY"]==company]["COMPANY"]
		logging.info("="*15 + f"kNN model - Test data READY" + "="*15)

		knn_model = KNeighborsClassifier(n_neighbors=1)
		logging.info("="*15 + f"kNN model being trained" + "="*15)
		# Train the model
		knn_model.fit(X_train, y_train)
		logging.info("="*15 + f"kNN model trained successfully" + "="*15)
		# Predict the response for test dataset
		y_pred = knn_model.predict(X_test)
		y_pred_proba = knn_model.predict_proba(X_test)
		y_pred_dist = knn_model.kneighbors(X_test)
		"""
		print(f"TEST DATA ORDER\n {y_train}")
		print(f"PREDICTION \n {y_pred}")
		print(f"PROBABILITIES \n {y_pred_proba}")
		dist = list(y_pred_dist[0])
		print(f"DISTANCE in same order as TEST DATA \n{dist}\n")
		"""
		logging.info("="*15 + f"kNN model predicted the most similar company to {company} successfully" + "="*15)
		test_comp = pd.DataFrame({"TOPIC_MODEL_VECTOR":list(X_test), "COMPANY":list(y_test), "SIMILAR_COMPANY":list(y_pred), "DISTANCE":list(y_pred_dist[0])})
		result = pd.concat([result, test_comp], ignore_index=True, axis=0)
	print(result)
	pickle(result, f"result_{feature}", "results")    

def generate_JSON(result_data, feature):
	companies = list(result_data["COMPANY"])
	nodes_with_values = {companies[i]:i for i in range(len(companies))}
	nodes = [{"name":i} for i in nodes_with_values.keys()]
	print(result_data["COMPANY"])
	result_data["LINKS"] = result_data.apply(lambda x: {"source":nodes_with_values[x["COMPANY"]],"target":nodes_with_values[x["SIMILAR_COMPANY"]]}, axis=1)
	links = list(result_data["LINKS"])
	graph = {"nodes":nodes,"links":links}
	print(graph)
	write_JSON(graph, f"result_{feature}", "results")
	
def make_data(feature):
    logging.info("="*15 + f"Unpickling of transformed {feature}" + "="*15)
    data = unpickle(f"test_{feature}", "transformed_feature_sets")
    companies = list(data["COMPANY"].unique())
    final_data = pd.DataFrame()
    for company in companies:
        logging.info("="*15 + f"{company} dataset - average of topic vectors being calculated" + "="*15)
        company_data_dist = data[data["COMPANY"]==company][["TOPIC_MODEL_VECTOR","COMPANY"]]
        comp_topic_vector = np.mean(company_data_dist["TOPIC_MODEL_VECTOR"])
        company_df = pd.DataFrame([[np.array(comp_topic_vector),company]], columns=["TOPIC_MODEL_VECTOR","COMPANY"])
        final_data = pd.concat([final_data, company_df], axis=0, ignore_index=True)
        logging.info("="*15 + f"{company} dataset - average obtained" + "="*15)
    pickle(final_data, f"final_data_{feature}", "final_data")

def main():
	feature = str(input("Enter feature .pkl file name in EXACT format:\n"))
	if TOPIC_MODELLING:
		logging.info("="*15 + "Topic modelling activated" + "="*15)
		topic_model(feature)
		logging.info("="*15 + "Topic modelling completed" + "="*15)
	if MAKE_DATASETS:
		logging.info("="*15 + "Building datasets" + "="*15)
		make_data(feature)
		logging.info("="*15 + "Datasets built" + "="*15)
	if KNN:
		logging.info("="*15 + "kNN model activated" + "="*15)
		final_data = unpickle(f"final_data_{feature}", "final_data")
		knn(final_data, feature)
		logging.info("="*15 + "Similar companies predicted" + "="*15)
	if GENERATE_JSON:
		logging.info("="*15 + f"JSON generation for {feature}" + "="*15)    
		result_data = unpickle(f"result_{feature}", "results")
		generate_JSON(result_data, feature)
		
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