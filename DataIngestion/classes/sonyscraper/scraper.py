import scrapy

class SonyScraper(scrapy.Spider):
    name="sony_scraper"
    custom_settings={
        'DOWNLOAD_DELAY':'3',
    }
    start_urls=['https://store.playstation.com/#!/en-us/all-ps4-games/cid=STORE-MSF77008-PS4ALLGAMESCATEG?emcid=pa-st-111690']

    def parse(
        self, response
        ):
        SET_SELECTOR='.statsText'
        number_of_pages='.statsText'
        for stat in response.css(SET_SELECTOR):
            PAGE_SELECTOR='span ::text'
            yield {
                'pages':stat.css(PAGE_SELECTOR).extract_first(),
            }
        SET_SELECTOR='.content'
        for game in response.css(SET_SELECTOR):
            IMAGE_SELECTOR='img'
            BADGESALE_SELECTOR='.badge ::text'
            yield {
                'image':game.css(IMAGE_SELECTOR).xpath('@src').extract(),
                'badge_sale':game.css(BADGESALE_SELECTOR).extract(),
            }