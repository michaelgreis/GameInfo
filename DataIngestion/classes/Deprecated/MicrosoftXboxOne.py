import scrapy
import os
import time as time
import json

class MicrosoftXboxoneScraper(scrapy.Spider,object):
    name="xbox_one_scraper"
    custom_settings={
        'DOWNLOAD_DELAY':'5',
    }
    start_urls=['https://www.xbox.com/en-US/games/xbox-one?xr=shellnav']

    def __init__(self):
        self.scraped_urls=[]
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120,550)

    def scrape(self):
        

