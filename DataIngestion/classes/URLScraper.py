import string #Dependencies: read_terms
import time as time #Dependencies: All - used for testing/performance monitoring
import os #Dependencies: read_terms
import urllib.request #Dependencies: url_scraper
import json
import binascii

class URLScraper():
    #initializing
    def __init__(self):
        self.scraper_terms = {} #configuration for any search terms needed by the scraper

#The purpose of this function is to remove non-ascii characters from a file.
    def remove_non_ascii(
        self,text_item
    ):
        return ''.join(i for i in text_item if ord(i)<128)


# The purpose of this is to read the list of search term/configurations for the URL hitting.
    def read_terms(
        self,filepath,source_name
        ):
        print(time.time())
        
        for filename in os.listdir(filepath): #loop through all files in the specified directory
            if source_name in filename:
                 with open(filepath+filename,'r') as file:
                    for line in file:
                        #line_unsplit = self.remove_non_ascii(line)
                        self.scraper_terms[source_name] = line.split("|")

        print("Scraper configuration successfully read for " + source_name + ".")
        print(time.time())

#the purpose of this to take a url which you desire to hit, what string will be altered, and hit the url repeatedly
    def url_scraper(
        self,fullurl,urlreplacestring,source_name,output_location
        ):
        
        os.chdir(output_location)
        with open(source_name+'.json','w', encoding='utf-8') as outfile:
       
            for key in self.scraper_terms:
                for item in self.scraper_terms[key]:
                    item = self.remove_non_ascii(item)
                    request_url = fullurl.replace("*",item)
                    #print(request_url)
                    req = urllib.request.Request(request_url, headers={'User-Agent': "Magic Browser"})
                    with urllib.request.urlopen(req) as response:
                        for line in response:
                            #decoded = line.decode('latin-1','xmlcharrefreplace') #binascii.b2a_base64(line,newline=True) # #this decoding was chosen at random.
                            #print(decoded)
                            json.dump(line.decode('utf-8','ignore'),outfile)
                            #json.dump(line.decode('utf-8','ignore')
                            # ,outfile)
        outfile.close()
