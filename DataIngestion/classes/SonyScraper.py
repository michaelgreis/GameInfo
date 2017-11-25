import scrapy
import os
import time as time
import json

class SonyScraper(scrapy.Spider):
    name="sony_scraper"
    custom_settings={
        'DOWNLOAD_DELAY':'5',
    }
    start_urls=['https://store.playstation.com/#!/en-us/all-ps4-games/cid=STORE-MSF77008-PS4ALLGAMESCATEG?emcid=pa-st-111690']
    
    def __init__(self):#,
        self.scraped_urls=['https://store.playstation.com/#!/en-us/all-ps4-games/cid=STORE-MSF77008-PS4ALLGAMESCATEG?emcid=pa-st-111690']


    def parse(
        self, response
        ):
        game_values = []
        SET_SELECTOR='.__desktop-presentation__grid-cell__base__0ba9f' 
        for game in response.css(SET_SELECTOR):
            IMAGE_SELECTOR='.product-image__img--main img'
            BADGESALE_SELECTOR='.price-display__price::text'
            GAMETITLE_SELECTOR='.grid-cell__title::text'
            game_values.append({
                'image':game.css(IMAGE_SELECTOR).xpath('@src').extract_first(),
                'badge_sale':game.css(BADGESALE_SELECTOR).extract_first(),
                'game_name':game.css(GAMETITLE_SELECTOR).extract_first(),
            })
        NEXTPAGE_SELECTOR='.paginator-control__page-number:not([class^="disabled"]) ::attr(href)'     #'.headPgCtl .pageLink:not([class^="pageLink inactive notLast selected"]) ::attr(href)'# .navlinks a ::attr(href)'
        next_page=response.css(NEXTPAGE_SELECTOR).extract()
        if next_page is not None:
            for url in next_page:
                if url not in self.scraped_urls:
                    yield scrapy.Request(
                        response.urljoin(url),
                        callback=self.parse
                    )
                    self.scraped_urls.append(url) #added to allow for skipping of already scraped web pages
        with open(self.name+str(time.time())+'.json','w', encoding='utf-8') as outfile:
                outfile.write(json.dumps(game_values))
        outfile.close()