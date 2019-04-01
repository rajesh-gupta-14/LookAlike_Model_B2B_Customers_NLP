#==========================================
# Title: Merging cleaned datasets for feature sets
# Author: Rajesh Gupta
# Date:   1 Mar 2019
#==========================================
import logging
from datetime import datetime
import csv, json
import os
import pandas as pd

from utility_functions import *
from global_vars import *

def merge_datasets(datasets=[], column=None):
	feature_df = pd.DataFrame()
	for each_dataset in datasets:
		company = each_dataset.loc[0, "COMPANY"]
		logging.info("="*15 + f"Merging for {company} {column}" + "="*15)
		feature_df = pd.concat([feature_df, each_dataset[[column, "COMPANY"]]], axis=0, ignore_index=True)
	return feature_df

if __name__ == "__main__":
	configure_logger()
	logging.info("="*15 + "Merging cleaned dataframes" + "="*15)
	# Appending all the cleaned company datasets to a list
	cleaned_datasets = [unpickle(company, "cleaned_data") for company in COMPANIES]
	for feature, _ in FEATURES.items():
		logging.info("="*15 + f"Generating {feature} set")
		feature_data = merge_datasets(cleaned_datasets, column=feature)
		pickle(feature_data, feature, "feature_sets")
		logging.info("="*15 + f"Successfully generated"+ "="*15)