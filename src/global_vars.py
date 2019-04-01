# imports
import os

# Company names
COMPANIES = ["Samsung", "Oracle", "IBM", "Intuit", "OpenText", "ICBC", "MicroStrategy", "Appian", "Symantec", "Pfizer", "Goldman Sachs", "Arista Networks", "Cognizant", "Deloitte", "Dropbox", "Freshdesk", "Informatica", "Shopify", "Spotify", "Symantec", "Toyota Motor", "VMware", "Zoho", "Amazon", "China Construction Bank", "Microsoft", "Accenture", "Apple", "Smartsheet", "Tech Mahindra", "Adobe Systems", "Walmart", "Netflix", "Morgan Stanley"]

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

# topic modelling iterations
NO_OF_ITERATIONS = 10000

# no of topics
NO_OF_TOPICS = 10