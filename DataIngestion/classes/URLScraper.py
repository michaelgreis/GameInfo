import string #Dependencies: read_terms
import time as time #Dependencies: All - used for testing/performance monitoring
import os #Dependencies: read_terms
import urllib.request #Dependencies: url_scraper
from bs4 import BeautifulSoup #Needed for the Sony scraper
import scrapy #Needed in order to delay the scraper for sony
#import json
#import re
#import binascii

class URLScraper():
    #initializing
    def __init__(self):
        self.scraper_terms = {} #configuration for any search terms needed by the scraper

#The purpose of this function is to remove non-ascii characters from a file.
    def remove_non_ascii(
        self,text_item
    ):
        return ''.join(i for i in text_item if ord(i)<128)

#The purpose of this function is to point to an online source for configuring scraper.
    def get_config_info(
        self,config_info_url
    ):
        req = urllib.request.Request(config_info_url, headers={'User-Agent': "Magic Browser"})
        config_http = urllib.request.urlopen(req)
        soup=BeautifulSoup(config_http)
        print(soup)


# The purpose of this is to read the list of search term/configurations for the URL hitting.
    def read_terms(
        self,filepath,source_name
        ):
        print(time.time())
        count=0
        for filename in os.listdir(filepath): #loop through all files in the specified directory
            if source_name in filename:
                with open(filepath+filename,'r') as file:
                    for line in file:
                        #line_unsplit = self.remove_non_ascii(line)
                        self.scraper_terms[source_name] = line.split("|")
                file.close()
        print("Scraper configuration successfully read for " + source_name + ".")
        print(time.time())
        print(len(set(self.scraper_terms[source_name])))

#the purpose of this to take a url which you desire to hit, what string will be altered, and hit the url repeatedly, pulling in the JSON.
    def url_scraper(
        self,fullurl,urlreplacestring,source_name,output_location,output_type
        ):
        os.chdir(output_location)
        
        if output_type.upper()=='JSON':
            search_list_count=len(set(self.scraper_terms[source_name])) #This is used to help with the formatting of the output file in urlscraper
            count=1
            with open(source_name+str(time.time())+'.json','w', encoding='utf-8') as outfile:
                outfile.write('[') #for JSON formatting. writing multiple times so need to make a list.
                for key in self.scraper_terms:
                    for item in set(self.scraper_terms[key]):
                        #if count<=3:
                        print(count)
                        item = self.remove_non_ascii(item)
                        request_url = fullurl.replace("*",item)
                        req = urllib.request.Request(request_url, headers={'User-Agent': "Magic Browser"})
                        with urllib.request.urlopen(req) as response:
                            for line in response:
                                if count==search_list_count:
                                    outfile.write(line.decode('utf-8','ignore'))
                                else:
                                    outfile.write(line.decode('utf-8','ignore')+',')
                        count+=1
                outfile.write(']')
            outfile.close()
        elif output_type.upper()=='BEAUTIFULSOUP': #outputs beautiful soup object
            print("Beautiful Soup")