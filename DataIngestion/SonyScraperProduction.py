#!/usr/bin/env python3.5
#PATH=/home/ubuntu/bin:/home/ubuntu/.local/bin:/usr/local/sbin:/usr/loc$
from classes.SonyScraper import SonyScraper
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
import os

print("Starting Scraper")
source_name='sonymarketplace'
data_output_location = "/crawler/data/"
print("Variables Loaded")

os.chdir(data_output_location)
#print("Directory Changed")

spider=SonyScraper()
process = CrawlerProcess()
process.crawl(spider)
process.start()
print("Scraper Finished")

