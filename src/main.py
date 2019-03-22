#==========================================
# Title: Company Similarity Analysis
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
from google_scraper import *
from twitter_scraper import *
				

def google_scraper():
	raw_data = pd.DataFrame()
	configure_logger()
	logging.info("============Script execution started============")
	for company in COMPANIES:
		company_data = pd.DataFrame()
		company_rows = 0
		logging.info("============{} data collection started============".format(company))
		for feature, feature_value in FEATURES.items():
			logging.info("============{}, {} feature data collection started============".format(company, feature))
			google_scraper = GoogleScraper(company, feature_value, COUNT)
			google_scraper.generate_google_src_code()
			hyperlinks = google_scraper.get_hyperlinks()
			raw_feature_data = google_scraper.get_raw_data(hyperlinks)
			if len(raw_feature_data)>company_rows:
				company_rows = len(raw_feature_data)
			raw_feature_data_df = pd.DataFrame(raw_feature_data, columns=[feature])
			company_data = pd.concat([company_data, raw_feature_data_df], axis = 1)
			logging.info("============{}, {} feature data collection completed============".format(company, feature))
		company_name = [company for each_count in range(company_rows)]
		company_name_df = pd.DataFrame(company_name, columns=["COMPANY"])
		company_data = pd.concat([company_data, company_name_df], axis=1)
		pickle(company_data, company, "raw_data")
		raw_data = pd.concat([raw_data, company_data], ignore_index=True)
		logging.info("============{} data collection completed============".format(company))	

	print(raw_data)
	#raw_data.to_csv(COMPANY_DATA_PATH, index=False)

def twitter_scraper():
	raw_twitter_data = pd.DataFrame()
	configure_logger()
	logging.info("============Script execution started============")
	for company in COMPANIES:
		twitter_handle = "@{}".format(company)
		tw = TwitterScraper(twitter_handle)
		tw.run_google_scraper()
		tw.get_twitter_hyperlinks()
		tweets = tw.get_tweets(number_of_tweets=TWEETS)
		tweets_df = pd.DataFrame(tweets, columns=["tweet"])
		company_name = [company for each_count in range(len(tweets))]
		company_name_df = pd.DataFrame(company_name, columns=["COMPANY"])
		tweets_df = pd.concat([tweets_df, company_name_df],axis=1)
		raw_twitter_data = pd.concat([raw_twitter_data, tweets_df], ignore_index=True)
	raw_twitter_data.to_csv(COMPANY_DATA_PATH, index=False)
	logging.info("============Script execution completed============")

def main(GOOGLE=0, TWITTER=0):
	if GOOGLE:
		google_scraper()
	if TWITTER:
		twitter_scraper()
	

if __name__ == "__main__":
	main(GOOGLE, TWITTER)