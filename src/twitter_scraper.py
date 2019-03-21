#==========================================
# Title: Google Web Scraping
# Author: Rajesh Gupta
# Date:   1 Mar 2019
#==========================================

from global_vars import *
import pandas as pd
from google_scraper import GoogleScraper
from utility_functions import *
from bs4 import BeautifulSoup
import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TwitterScraper(GoogleScraper):

    chromedriver_path = CHROMEDRIVERPATH
    headerless_option = HEADERLESS

    def __init__(self, company_name):
        super().__init__(company_name)
        self.stripped_company_name = self.company_name.replace("@","")
    
    # Run the google scraper to get hyperlinks
    def run_google_scraper(self):
        super().generate_google_src_code()
        super().get_hyperlinks()
        
    # Get the hyperlinks specific to twitter
    def get_twitter_hyperlinks(self, hyperlinks=None):
        logging.info("============Twitter hyperlink extraction started============")
        if hyperlinks is None:
            hyperlinks = self.hyperlinks
        self.twitter_hyperlinks = [hyperlink[:hyperlink.lower().find(self.stripped_company_name.lower())
                                        +len(self.stripped_company_name.lower())]
                                        for hyperlink in hyperlinks if "twitter" in hyperlink]
        logging.info("============Twitter hyperlink extraction completed============")
        return self.twitter_hyperlinks

    # Get tweets for hyperlinks
    def get_tweets(self, number_of_hyperlinks=1, number_of_tweets=100):
        for index in range(number_of_hyperlinks):
            try:
                logging.info("============Tweets extraction for {} started============".format(self.company_name))
                self.setup_selenium(self.twitter_hyperlinks[index], headerless = HEADERLESS)
                self.get_url_of_hyperlink()
                self.raw_data = self.get_tweet_texts(number_of_tweets)
                self.quit()
                return self.raw_data
            except Exception as e:
                #print(e)
                continue

    # Set URL and config options of selenium
    def setup_selenium(self, url, headerless = False):
        logging.info("============Selenium URL set:{}============".format(url))
        self.url = url
        self.options = Options()
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.options.add_experimental_option("prefs", prefs)    
        if headerless:
            self.options.add_argument("--headless")
        logging.info("============Selenium Invoked============")
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path=CHROMEDRIVERPATH)

    # Get URL of hyperlink
    def get_url_of_hyperlink(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "tweet-text")))
    
    # Get source code of hyperlink
    def get_tweet_texts(self, max_count):
        self.tweets = []
        prev_length = 0
        flag=-1
        while prev_length<max_count and flag!=0:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                WebDriverWait(self.driver, 5).until(lambda driver: self.check()!=prev_length, "Previous and current count equal")
            except:
                logging.info("""============Previous and current tweet count equal. It is possible
                that the number of tweets you are looking for is not available============""")
                flag = 0
            prev_length = self.check()
            logging.info("============{} tweets obtained for {}============"
                            .format(prev_length,self.stripped_company_name))

        for each_tweet_block in self.tweet_blocks:
            tweet = each_tweet_block.text
            self.tweets.append(tweet[:tweet.find("http")])
        
        return self.tweets

    # check if prev len of tweets when scrolled is same as current len of tweets
    def check(self):
        self.twitter_src_code = self.driver.execute_script("return document.body.innerHTML;").encode("ascii","ignore").decode("utf-8").encode("utf-8")
        self.twitter_soup = BeautifulSoup(self.twitter_src_code, 'html.parser')
        self.tweet_blocks = self.twitter_soup.find_all("p",{"class":"tweet-text"})
        return len(self.tweet_blocks)

    # close browser
    def quit(self):
        self.driver.quit()