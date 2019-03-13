# imports
import os

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