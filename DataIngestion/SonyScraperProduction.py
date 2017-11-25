from classes.SonyScraper import SonyScraper
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
import os

source_name='sonymarketplace'
data_output_location = "OutputFiles/"#"/crawler/data/"

os.chdir(data_output_location)

spider=SonyScraper()
process = CrawlerProcess()
process.crawl(spider)
process.start()
