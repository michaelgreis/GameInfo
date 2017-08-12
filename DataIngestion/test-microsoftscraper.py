from classes import URLScraper as URLS
import time as time


print("Test Started")
print(time.time())

input_file_path = "configfiles/"
source_name = "marketplace.xbox.com"
full_url = "http://marketplace.xbox.com/en-US/SiteSearch/xbox/?query=[*]&PageSize=1000000"
data_output_location = "outputfiles/"

microsoftscraper = URLS.URLScraper()

microsoftscraper.read_terms(input_file_path,source_name)

microsoftscraper.url_scraper(full_url,"*",source_name,data_output_location)

print("Test Completed")
print(time.time())