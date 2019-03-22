#==========================================
# Title: Cleaning scripts
# Author: Rajesh Gupta
# Date:   1 Mar 2019
#==========================================
from utility_functions import *
from global_vars import *
import re, pandas as pd
import logging

class DataCleaning:

    def __init__(self):
        self.js = re.compile(r'<script.*?>.*?</script>')
        self.css = re.compile(r'<style.*?>.*?</style>')
        self.html = re.compile(r'<.*?>')
        self.braces = re.compile(r'{.*?}')
        self.spl_symbols = re.compile(r'&\S*?;|[\\\/\_\(\)\|\>\<\%]|\.async\-hide')
        self.spaces = re.compile(r'\s+')
        self.urls = re.compile(r'https?\:\/\/.*?\s')

    def clean_js(self, df, columns=None):
        """
        Aliter : PLEASE NOTE THAT THIS CAN BE AN ALITER TO ALL FUNCTIONS IN THIS CLASS.
        if columns is not None:
            y=[]
            for x in columns:
                y.append(self.js.sub(" ", str(df[x])))
            return pd.Series(y)
        """
        logging.info("="*15+"Cleaning JS"+"="*15)
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_js(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.js.sub(" ", str(df))

    def clean_html(self, df, columns=None):
        logging.info("="*15+"Cleaning HTML"+"="*15)
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_html(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.html.sub(" ", str(df))

    def clean_css(self, df, columns=None):
        logging.info("="*15+"Cleaning CSS"+"="*15)
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_css(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.css.sub(" ", str(df))

    def clean_braces(self, df, columns=None):
        logging.info("="*15+"Cleaning braces"+"="*15)
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_braces(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.braces.sub(" ", str(df))

    def clean_special_symbols(self, df, columns=None):
        logging.info("="*15+"Cleaning special symbols"+"="*15)
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_special_symbols(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.spl_symbols.sub(" ", str(df))

    def clean_spaces(self, df, columns=None):
        logging.info("="*15+"Cleaning spaces"+"="*15)
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_spaces(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.spaces.sub(" ", str(df))

    def clean_urls(self, df, columns=None):
        logging.info("="*15+"Cleaning URLs"+"="*15)
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_urls(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.urls.sub(" ", str(df))

if __name__ == "__main__":
    configure_logger()
    logging.info("="*15 + "Cleaning script started"+ "="*15)
    # Put a for loop to iterate over the collected and pickled files here
    for company in COMPANIES:
        logging.info("="*15 + f"Unpickling of {company}"+ "="*15)
        data = unpickle(company, "raw_data")
        clean = DataCleaning()
        columns = list(FEATURES.keys())
        # Even this can be used as an alternative to applymap
        # data[columns] = data[columns].apply(lambda x: clean.clean_js(x, columns=columns), axis=1)
        logging.info("="*15 + "Cleaning JS"+ "="*15)
        data[columns] = data[columns].applymap(lambda x: clean.clean_js(x))
        logging.info("="*15 + "Cleaning CSS"+ "="*15)
        data[columns] = data[columns].applymap(lambda x: clean.clean_css(x))
        logging.info("="*15 + "Cleaning HTML"+ "="*15)
        data[columns] = data[columns].applymap(lambda x: clean.clean_html(x))
        logging.info("="*15 + "Cleaning the braces"+ "="*15)
        data[columns] = data[columns].applymap(lambda x: clean.clean_braces(x))
        logging.info("="*15 + "Cleaning the URLs"+ "="*15)
        data[columns] = data[columns].applymap(lambda x: clean.clean_urls(x))
        logging.info("="*15 + "Cleaning the special symbols"+ "="*15)
        data[columns] = data[columns].applymap(lambda x: clean.clean_special_symbols(x))
        logging.info("="*15 + "Cleaning the spaces"+ "="*15)
        data[columns] = data[columns].applymap(lambda x: clean.clean_spaces(x))
        logging.info("="*15 + "Filling NaNs (nan string due to str(df) in clean fns) and blanks with 0"+ "="*15)
        data[columns] = data[columns].replace("nan", 0)
        data[columns] = data[columns].replace(" ", 0)
        logging.info("="*15 + f"{company} data cleaned"+ "="*15)
        pickle(data, company, "cleaned_data")
        print(data)