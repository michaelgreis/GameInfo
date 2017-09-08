from classes import URLScraper as URLS
import time as time

print("Test Started")
print(time.time())

sony_scraper=URLS.URLScraper()

sony_scraper.get_config_info("https://store.playstation.com/#!/en-us/all-ps4-games/cid=STORE-MSF77008-PS4ALLGAMESCATEG?emcid=pa-st-111690")