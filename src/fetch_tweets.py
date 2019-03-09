#==========================================
# Title:  Use REST API calls to fetch tweets
# Author: Rajesh Gupta
# Date:   1 Oct 2018
#==========================================

import tweepy
import json, csv
import time
import logging
from global_vars import *

class FetchTwitterData():
	def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
		print("Authenticating with the Twitter API...")
		self.consumer_key=consumer_key
		self.consumer_secret=consumer_secret
		self.access_key=access_key
		self.access_secret=access_secret
		self.OAuth()

	def OAuth(self):
		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_key, self.access_secret)
		self.api = tweepy.API(self.auth)

	def get_profile(self, screen_name):
		self.screen_name = screen_name
		try:
			self.user_profile = self.api.get_user(self.screen_name)
		except tweepy.error.TweepError as e:
			self.user_profile = json.loads(e.response.text)
		return self.user_profile

	def get_user_tweets(self, screen_name):
		self.screen_name = screen_name
		try:
			self.user_tweets = self.api.user_timeline(self.screen_name)
		except tweepy.error.TweepError as e:
			self.user_tweets = json.loads(e.response.text)
		return self.user_tweets

	def get_trends(self, location_id):
		self.location_id=location_id
		try:
			self.trends = self.api.trends_place(self.location_id)
		except tweepy.error.TweepError as e:
			self.trends = json.loads(e.response.text)
		return self.trends

	def get_tweets(self, search_query):
		print("Fetching tweets by keyword: {}".format(search_query))
		self.search_query = search_query
		try:
			self.tweets = self.api.search(self.search_query,lang="en",count=1000)
		except tweepy.error.TweepError as e:
			self.tweets = [json.loads(e.response.text)]
		return self.tweets