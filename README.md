# Look-alike modeling for B2B customers #

## Author: ##
* Rajesh Gupta - rajesh.gupta@dal.ca (Owner)

## Description: ##
This repository hosts the code to scrape data from Google and Twitter, clean data, reduce the dimensions of data and construct a look-alike model. The look-alike model uses KNN to identify similar companies from the existing customer base based on certain characteristics. The characteristics include products developed, the technology stack, the size, the acquisitions and future goals of a company.

### Required packages: ###
* bs4
* sklearn
* nltk
* requests
To install the packages, run: ```pip install <package_name>```

## How to execute the program: ##
Firstly, configure the characteristics/features using relevant keywords in global_vars.py file.

### Data Collection ###
- Configure the TWITTER and GOOGLE boolean variables in global_vars.py file to run either or both of the custom scrapers.
- Run the command in the command prompt/terminal:  ```python main.py```
- Output is stored in a serialized format in src/raw_data

### Data Cleaning ###
- Run this command to clean Google data in the command prompt/terminal: ```python clean_data.py```
- Run this command to clean Twitter data in the command prompt/terminal: ```python clean_twitter_data.py```
- Input taken is src/raw_data and output is stored in serialized format in src/cleaned_data

### Data Merging ###
- Run this command to merge the data of companies and split them according to the appropriate characteristic/feature in the command prompt/terminal: ```python merge_data.py```
- Input taken is src/cleaned_data and output is stored in serialized format in src/feature_sets

### Data Dimensionality Reduction ###
- Configure the TOPIC_MODLELING, NO_OF_ITERATIONS, NO_OF_TOPICS variables to activate the topic modeling module, and the iterations and size of topic vector.
- Run this command to construct topic vectors and reduce the data dimensions in the command prompt/terminal: ```python topic_modelling.py```
- Input taken is src/feature_sets and output is stored in serialized format in src/transformed_feature_sets

### KNN modeling ###
- Configure the KNN, MAKE_DATASETS variable to activate the Knn algorithm and generate suitable training data for Knn.
- Run this command to construct the model and output results in the command prompt/terminal: ```python topic_modelling.py```
- Input taken is src/transformed_feature_sets and output is stored in serialized format in src/final_data

## References ##
[1] R. Pandey, "Digitalxplore.org," 2017. [Online]. Available: http://www.digitalxplore.org/up_proc/pdf/283-14906064304-6.pdf.<br/>
[2] "Analytics in Marketing - Measure, Analyze, and Manage", Wordstream.com, 2019. [Online]. Available: https://www.wordstream.com/marketing-analytics.<br/>
[3] T. Mikolov, I. Sutskever, K. Chen, G. Corrado and J. Dean, "Distributed representations of words and phrases and their compositionality", Dl.acm.org, 2019. [Online]. Available: https://dl.acm.org/citation.cfm?id=2999959.<br/>
[4] H. Jelodar et al., "Latent Dirichlet Allocation (LDA) and Topic modeling: models, applications, a survey", arXiv.org, 2019. [Online]. Available: https://arxiv.org/abs/1711.04305.<br/>
[5]"Documentation scikit-learn: machine learning in Python — scikit-learn 0.20.3 documentation", Scikit-learn.org, 2019. [Online]. Available: https://scikit-learn.org/stable/documentation.html.<br/>
[6] N. Bölücü and B. Can, "Unsupervised Joint PoS Tagging and Stemming for Agglutinative Languages", ACM Transactions on Asian and Low-Resource Language Information Processing, vol. 18, no. 3, pp. 1-21, 2019. Available: 10.1145/3292398.<br/>
[7] D. Yu and A. Houg, "Facebook Analytics, Advertising, and Marketing", Facebook Nation, pp. 117-138, 2014. Available: 10.1007/978-1-4939-1740-2_6.<br/>

I sincerely thank Brakadeesh Shankar, Anurag Sreekumar, and Karthik Parameswaran for their contribution in helping me test out the various modules.
