from utility_functions import *
from global_vars import *
import re, pandas as pd
import logging

class DataCleaning:

    def __init__(self):
        self.js = re.compile(r'<script.*>.*?</script>')
        self.html = re.compile(r'<.*?>')
        self.braces = re.compile(r'{.*?}')
        self.spl_symbols = re.compile(r'&\S*?;')
        self.spaces = re.compile(r'\s+')

    def clean_js(self, df, columns=None):
        """
        Aliter : PLEASE NOTE THAT THIS CAN BE AN ALITER TO ALL FUNCTIONS IN THIS CLASS.
        if columns is not None:
            y=[]
            for x in columns:
                y.append(self.js.sub(" ", str(df[x])))
            return pd.Series(y)
        """
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_js(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.js.sub(" ", str(df))

    def clean_html(self, df, columns=None):
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_html(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.html.sub(" ", str(df))

    def clean_braces(self, df, columns=None):
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_braces(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.braces.sub(" ", str(df))

    def clean_special_symbols(self, df, columns=None):
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_special_symbols(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.spl_symbols.sub(" ", str(df))

    def clean_spaces(self, df, columns=None):
        if columns is not None:
            df = df[columns].to_frame().applymap(lambda x: self.clean_spaces(x))
            return df.T.iloc[0,:] # df.squeeze() will also do
        return self.spaces.sub(" ", str(df))

if __name__ == "__main__":
    configure_logger()
    logging.info("="*15 + "Cleaning script started"+ "="*15)
    # Put a for loop to iterate over the collected and pickled files here
    logging.info("="*15 + "Unpickling of {}"+ "="*15)
    data = unpickle("0_companies_data_pd")
    write_file(str(data.iloc[-1,1]), filename="trial.txt")
    clean = DataCleaning()
    columns = list(FEATURES.keys())
    # Even this can be used as an alternative to applymap
    # data[columns] = data[columns].apply(lambda x: clean.clean_js(x, columns=columns), axis=1)
    logging.info("="*15 + "Cleaning JS"+ "="*15)
    data[columns] = data[columns].applymap(lambda x: clean.clean_js(x))
    logging.info("="*15 + "Cleaning HTML"+ "="*15)
    data[columns] = data[columns].applymap(lambda x: clean.clean_html(x))
    logging.info("="*15 + "Cleaning the braces"+ "="*15)
    data[columns] = data[columns].applymap(lambda x: clean.clean_braces(x))
    logging.info("="*15 + "Cleaning the special symbols"+ "="*15)
    data[columns] = data[columns].applymap(lambda x: clean.clean_special_symbols(x))
    logging.info("="*15 + "Cleaning the spaces"+ "="*15)
    data[columns] = data[columns].applymap(lambda x: clean.clean_spaces(x))
    print(data)

