from classes import URLScraper as URLS
import time as time
from classes.spiders import spider

print("Test Started")
print(time.time())
url="https://store.playstation.com/#!/en-us/all-ps4-games/cid=STORE-MSF77008-PS4ALLGAMESCATEG?emcid=pa-st-111690"

#sony_scraper=URLS.URLScraper()

#sony_scraper.get_config_info(url)

sony_spider=spider.DelayedSpider()
sony_spider.parse(url)