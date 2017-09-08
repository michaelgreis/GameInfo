import scrapy

class DelayedSpider(scrapy.Spider):
    name = "DelayedSpider"

    custom_settings = {
        'DOWNLOAD_DELAY': 5, #delay in seconds for the scraper
    }

    def start_requests( #https://stackoverflow.com/questions/14017996/is-there-a-way-to-pass-optional-parameters-to-a-function
        self,request_url,parameter_list,**keyword_parameters
    ):
        if ('optional' in keyword_parameters):
            scrapy.Request(url=request_url, callback=self.parse)
        else:
            
    def parse_request(
        self,response
    ):
    