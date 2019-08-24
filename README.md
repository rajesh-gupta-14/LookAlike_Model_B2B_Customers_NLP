# sentimet-analysis-using-lexicon #

## Authors: ##
* Rajesh Gupta - rajesh.gupta@dal.ca
* Vismay Revankar - vismayhr@dal.ca

## Description: ##
This repository hosts the code for a lexicon based sentiment analyser. The lexicon used is [SentiWordNet](http://sentiwordnet.isti.cnr.it/). The data set used is a collection of ~1000 tweets fetched used the tweepy package. The program implements 2 approaches to sentiment analysis:
* Average based approach
* Using [Pointwise Mutual Information](https://www.computer.org/csdl/proceedings/icoit/2016/3584/00/07966838.pdf) (PMI)

The average based approach involves finding the score of every word in a tweet from the lexicon; summing all scores of words in the tweet and finding the average score. If the score in positive, it implies that the tweet has a positive sentiment. A negative score implies the tweet is negative in sentiment and 0 indicates a neutral tweet. 

An explanation of the PMI approach can be viewed in the cited research paper.

## How to execute the program: ##
Generate and store the required credentials for tweepy and Elastic search as mentioned in the global_vars.py file.
<br>
Run the command in the command prompt/terminal:  ```python main.py```

**NOTE: It is required to use the sentiwordnet file provided in this repository to run the code successfully.**  
<br>
We have edited certain portions of the file to make it easier to convert it into CSV format (The first ~20 lines have containing information about the lexicon have been removed). However, no changes have been made to the words or their corresponding scores in the lexicon, hence, the results will not be affected in anyway.

### Required packages: ###
* tweepy
* elasticsearch
* matplotlib
* seaborn
To install the packages, run: ```pip install <package_name>```

### Brief code walk-through ###
* **basic_avg_analysis.py** : This file contains our implementation of Sentiment Analysis by averaging the sentiment scores of all words in a given tweet.
* **clean_twitter_data.py** : The CleanTwitterData class is used to perform data cleaning on the raw twitter data. It cleans the data using regex.
* **fetch_tweets.py** : This script uses the tweepy package to authenticate with Twitter and fetch tweets.
* **global_vars.py** : This file is used to store global variables that are required during the execution of the program.
* **main.py** : This is the main() function of the application.
* **plot_graph.py** : This script is used to fetch the results of the 2 sentiment analysis programs and plot the data on a graph.
* pointwise_mutual_information.py : This class consists of the implementation of the seconds sentiment analysis algorith i.e., Pointwise Mutual Information.
* **upload_to_elasticsearch_search_server** : This class takes care of the operations involved in uploading the analysis results to the Elastic Search intance.
* **utility_functions** : The functions in this file are used general-purpose operations such as converting to CSV, etc.

#### Generated files: ####
* **combined_analysis.json** : The outputs of both analyses are written into this file in the form of JSON. This data is then uploaded onto the Elastic Search server.
* **raw_twitter_data.csv** : This file stores the raw, uncleaned tweets fetched using the tweepy package.
* **sentiwordnet_dictionary.csv** : This file stores only the relevant information from the SentiWordNet lexicon in the form of CSV. The contents of this file are used to perform the first analysis, i.e., using averages.
* **log files** : The logs can be found in the \logs folder. We have made an extensive effort to log every operation and calculation performed during the analysis.
files in \plot_data : This folder contains two files into which the sentiment analysis programs write the results. These results are then parsed by plot_graph.py and a graph is plotted. This graph is stored in the same folder too.