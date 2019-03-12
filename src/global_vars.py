# imports
import os
######
# Twitter API credentials
CONSUMER_KEY = "eRvtkP6oXaUK6ZiCKCnOPujQ8"
CONSUMER_SECRET = "91vze0F0XCeNw442JWtW7vQdN36fAthDcfsXAhOCuM3KScvGQK"
ACCESS_KEY = "1044693780224462849-sgHwgJaSKB5Vm9C6R9yKsHlApxdwlx"
ACCESS_SECRET = "XP9kVkHm8b7DAqqDi3CqSm4JznLdCc0yNrXpkWVM7JaBD"

# User Query
TWITTER_QUERIES = ["Apple","Samsung"]

# Raw Twitter Data CSV filename
TWITTER_DATA_CSV = "raw_twitter_data.csv"
#############
## START
# Company names
COMPANIES = ["IBM", "Oracle"]

# Features
FEATURES = {
    "SIZE" : ["\"size\"", "\"number of employees\"", "\"employees\""],
    "ACQUISITIONS" : ["\"acquire\"", "\"take over\"", "\"took over\"","\"acquisition\""]
    }

# Number of Google results
COUNT = 10

# Company Data CSV filename
COMPANY_DATA_PATH = "company_data.csv"

# Chromedriver path
CHROMEDRIVERPATH = "D:/MACS/nlp/Project/company-analysis-env/project-code/src/chromedriver.exe"

# Headerless boolean
HEADERLESS = False

# Google and Twitter enabler
GOOGLE = 0
TWITTER = 1

# Number of tweets needed
TWEETS = 200