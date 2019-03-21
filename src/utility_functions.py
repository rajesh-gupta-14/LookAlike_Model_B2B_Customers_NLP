#==========================================
# Title:  Utility function for logging and CSV conversion
# Author: Rajesh Gupta
# Date:   1 Oct 2018
#==========================================

from datetime import datetime
import logging
import csv
import json
import os
from global_vars import *
import pickle as pkl

def configure_logger():
	current_datetime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
	fpath = os.path.join(os.getcwd(),"logs\company_analysis_log-{}.txt".format(current_datetime))
	log_file = fpath
	log_stream = 'sys.stdout'
	log_level = logging.DEBUG
	log_format = "%(asctime)s %(levelname)s: %(message)s"
	log_date_format = "%m/%d/%Y %H:%M:%S"
	logging.basicConfig(filename=log_file, level=log_level, format=log_format, datefmt=log_date_format)
	
def write_raw_twitter_data_to_csv(raw_twitter_data):
	logging.info("Writing raw twitter data to CSV format: {}".format(TWITTER_DATA_CSV))
	with open(TWITTER_DATA_CSV,'w') as f:
		csvwriter = csv.writer(f, lineterminator="\n")
		csvwriter.writerow(['id','user','created_at','text'])
		for raw_tweets in raw_twitter_data:
			for tweet in raw_tweets:
				csvwriter.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode("ascii","ignore").decode("utf-8")])

def get_raw_tweets_from_csv():
	logging.info("Fetching raw tweets from the CSV file")
	raw_tweets = []
	with open(TWITTER_DATA_CSV,"r") as f:
		csv_reader = csv.DictReader(f)
		for each_line in csv_reader:
			raw_tweets.append(each_line['text'])
	return raw_tweets


def write_file(text, filename):
	with open(filename,"w") as f:
		f.write(text)

def read_file(filename):
	with open(filename, "r") as f:
		data = f.read()
	return data
	
def pickle(obj, filename, foldername):
	COMPANYPKLPATH = os.path.join(os.getcwd(), foldername, filename + ".pkl") 
	with open(COMPANYPKLPATH, "wb") as f:
		pkl.dump(obj, f)

def unpickle(filename, foldername):
	COMPANYPKLPATH = os.path.join(os.getcwd(), foldername, filename + ".pkl")
	with open(COMPANYPKLPATH, "rb") as f:
		data = pkl.load(f)
	return data