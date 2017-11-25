from classes.SonyScraper import SonyScraper
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess

import os
import time as time


print("Test Started")
print(time.time())
source_name='sonymarketplace'
data_output_location = "outputfiles/"

os.chdir(data_output_location)

spider=SonyScraper(
    #output_directory=data_output_location,
    #source_name=source_name
    )

process = CrawlerProcess()
#process.crawl(SonyScraper(output_location=data_output_location,source_name=source_name))
process.crawl(spider)
process.start()

#process=CrawlerProcess()
#process.crawl(spider)
#process.start()
