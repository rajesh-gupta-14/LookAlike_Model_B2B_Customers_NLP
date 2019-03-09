#==========================================
# Title:  Clean and format raw tweets using regex
# Author: Rajesh Gupta
# Date:   2 Oct 2018
#==========================================

import csv, re
from math import log2
import logging
from global_vars import *

class CleanTwitterData():
	
	def __init__(self):
		print("Cleaning the tweets to retain only textual content")
		self.compile_regex_patterns()
		
	def compile_regex_patterns(self):
		self.cleaning_patterns = {
			"removes_username" : (re.compile(r'@\w+'),' '), #removes user names from tweet
			"remove_urls":(re.compile(r'https?://\S*'),''), #removes urls
			"remove_rt": (re.compile(r'\brt\b|\.'),''), #removes retweets and fullstops
			"remove_single_char": (re.compile(r'\s[a-z]\s'),' '), #removes single alphabets a-z
			"sub_nt_with_not": (re.compile(r'n\'t'),' not'), #removes n't with not
			"removes_special_char": (re.compile(r'[\:\(\)\[\]$#-]'),' '), #removes emojis and special characters
			"remove_all_but_alpha": (re.compile(r'[^a-z\d\s]'),' '), #removes everything except alphabets, digits and spaces
			"remove_extra_whitespaces":(re.compile(r'\s+'),' '), #removes additional whitespaces
		}
			
	def clean_with_regex(self, unclean_tweets):
		logging.info("Cleaning twitter data....")
		clean_tweets = []
		for tweet in unclean_tweets:
			tweet = tweet.lower() #converting all alphabets to lowercase
			for remove_key, pattern in self.cleaning_patterns.items():
				tweet=pattern[0].sub(pattern[1],tweet)
			clean_tweets.append(tweet.strip())
		return clean_tweets