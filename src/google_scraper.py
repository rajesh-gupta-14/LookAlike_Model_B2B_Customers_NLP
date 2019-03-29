#==========================================
# Title: Google Web Scraping
# Author: Rajesh Gupta
# Date:   1 Mar 2019
#==========================================

from bs4 import BeautifulSoup
import requests
import logging

class GoogleScraper():

    headers = {'Accept-Encoding': 'gzip, deflate'}

    def __init__(self, company_name, any_of_these=[], count=10):
        logging.info("=====================Setting company variables for Google Search===================")
        self.company_name = company_name
        self.any_of_these = " ".join(any_of_these)
        self.count = count
        self.google_url = """https://www.google.com/search?hl=en&as_q=&as_epq={0}&as_oq={1}&as_eq=
        &as_nlo=&as_nhi=&lr=lang_en&cr=&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=
        &as_rights=&num={2}""".format(self.company_name, self.any_of_these, self.count)
        
    # Generate the source code of google search page
    def generate_google_src_code(self):
        logging.info("======================Generating Google Search code==========================")
        response = requests.get(self.google_url, headers=GoogleScraper.headers, verify=False)
        self.google_src_code = response.text.encode("ascii","ignore").decode("utf-8")
        return self.google_src_code

    # Get the search result hyperlinks from google source code
    def get_hyperlinks(self):
        logging.info("=========================Getting search result hyperlinks========================")
        self.soup = BeautifulSoup(self.google_src_code, 'html.parser')
        links = [each_result.find_all("a")[0]["href"] 
                        for each_result in self.soup.find_all("h3",{"class":"r"})]
        self.hyperlinks = [link[7:link.find("&")] for link in links if "http" in link]
        return self.hyperlinks

    # Get raw source code (data) from the hyperlinks
    def get_raw_data(self, hyperlinks=None):
        if hyperlinks is None:
            hyperlinks = self.hyperlinks
        logging.info("=========================Getting search result source code=========================")
        raw_data = []
		for hyperlink in hyperlinks:
			try:
				html_code = str(requests.get(hyperlink, headers=GoogleScraper.headers, verify=False).text.encode("ascii","ignore").decode("utf-8")).replace("\n","").replace(",","")
				raw_data.append(html_code)
			except:
				logging.info("="*15+ "URL skipped" + "="*15)
				continue
        return raw_data