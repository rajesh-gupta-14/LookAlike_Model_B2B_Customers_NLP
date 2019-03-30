# imports
import os

# Company names
COMPANIES = ["SAP"]

# Features
FEATURES = {
    "SIZE" : ["\"size\"", "\"number of employees\"", "\"employees\""],
    "ACQUISITIONS" : ["\"acquire\"", "\"take over\"", "\"took over\"","\"acquisition\""],
    "FUTURE GOALS" : ["\"future\"", "\"goals\"", "\"future goals\"", "\"aim\"", "\"ambition\"", "\"objectives\"", "\"deals\""],
    "TECH STACK" : ["\"technology\"","\"stack\"","\"stack\"","\"development tools\""],
    "PRODUCTS" : ["\"products\"", "\"services\"", "\"applications\"", "\"software\"", "\"tools\""]
    }

# Number of Google results
COUNT = 10

# Company Data CSV filename
COMPANY_DATA_PATH = os.path.join(os.getcwd(), "twitter_data", "company_data.csv")

# Chromedriver path
CHROMEDRIVERPATH = os.path.join(os.getcwd(), "driver", "chromedriver.exe")

# Headerless boolean
HEADERLESS = False

# Google and Twitter enabler
GOOGLE = 1
TWITTER = 0

# Number of tweets needed
TWEETS = 200

# Modelling
TOPIC_MODELLING = 1

# Make datasets
MAKE_DATASETS = 0

# Knn model activation
KNN = 0

# Iterations for topic modelling - Do not go above 10000
NO_OF_ITERATIONS = 10000

# Number of topics to be extracted
NO_OF_TOPICS = 10