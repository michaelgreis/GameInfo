import scrapy
import os
import time as time
import json

#added to get output pipeline in place.
from ..items import SonyItem, SonyItemLoader

def load_product(response):
    loader = SonyItemLoader(item=SonyItem(),response=response)

    game_values = {}
    SET_SELECTOR='.__desktop-presentation__grid-cell__base__0ba9f' 
    for game in response.css(SET_SELECTOR):
        IMAGE_SELECTOR='.product-image__img--main img'
        BADGESALE_SELECTOR='.price-display__price::text'
        GAMETITLE_SELECTOR='.grid-cell__title > span::text'
        PLUS_BADGESALE_SELECTOR='.price-display__price--is-plus-upsell::text'
        CONSOLE_TYPE_SELECTOR='.grid-cell__left-detail--detail-1::text'
        ITEM_TYPE_SELECTOR='.grid-cell__left-detail--detail-2::text'

        #loader.add_value('image',game.css(IMAGE_SELECTOR).xpath('@src').extract_first())
        #loader.add_value('badge_sale',game.css(BADGESALE_SELECTOR).extract_first())
        #loader.add_value('game_name',game.css(GAMETITLE_SELECTOR).extract_first())
        #loader.add_value('plus_sale',game.css(PLUS_BADGESALE_SELECTOR).extract_first())
        #loader.add_value('console_type',game.css(CONSOLE_TYPE_SELECTOR).extract_first())
        #loader.add_value('item_type',game.css(ITEM_TYPE_SELECTOR).extract_first())

        #removed in favor of item loader.
        if game.css(PLUS_BADGESALE_SELECTOR).extract_first() is not None:
            plus_sale = game.css(PLUS_BADGESALE_SELECTOR).extract_first()
        else:
            plus_sale = 'Not Available'
        
        if game.css(BADGESALE_SELECTOR).extract_first() is not None:
            badge_sale = game.css(BADGESALE_SELECTOR).extract_first()
        else:
            badge_sale = 'Not Available'
        
        if game.css(ITEM_TYPE_SELECTOR).extract_first() is not None:
            item_type = game.css(ITEM_TYPE_SELECTOR).extract_first()
        else:
            item_type = 'Not Available'
        
        game_values.update({
            'image':game.css(IMAGE_SELECTOR).xpath('@src').extract_first(),
            'badge_sale':badge_sale,
            'game_name':game.css(GAMETITLE_SELECTOR).extract_first(),
            'plus_sale':plus_sale,
            'console_type':game.css(CONSOLE_TYPE_SELECTOR).extract_first(),
            'item_type':item_type,
        })
        loader.add_value(None,game_values)
        #-------------
        
        #NEXTPAGE_SELECTOR='.paginator-control__page-number:not([class^="disabled"]) ::attr(href)'     #'.headPgCtl .pageLink:not([class^="pageLink inactive notLast selected"]) ::attr(href)'# .navlinks a ::attr(href)'
        #next_page=response.css(NEXTPAGE_SELECTOR).extract()
        #if next_page is not None:
        #    for url in next_page:
                #yield self.parse
                #yield response.follow(url,self.parse)
                #if url not in self.scraped_urls:
        #            response.follow(url,self.parse)
                    #yield scrapy.Request(
                    #    response.urljoin(url),
                    #    callback=self.parse
                    #)
                    #self.scraped_urls.append(url) #added to allow for skipping of already scraped web pages
        return loader.load_item()

class SonyScraperSpider(scrapy.spiders.CrawlSpider):
    name="sony_scraper"
    start_urls=['https://store.playstation.com/en-us/grid/STORE-MSF77008-ALLGAMES/1']
    allowed_domains=['store.playstation.com']
    rules = (
        scrapy.spiders.Rule(scrapy.linkextractors.LinkExtractor(allow=(r"store.playstation.com/en-us/grid/STORE-MSF77008-ALLGAMES/")),
        callback='parse_product',
        follow=True),
    )
    
    #custom_settings={
    #    'DOWNLOAD_DELAY':'1',
    #}
    #start_urls=['https://store.playstation.com/#!/en-us/all-ps4-games/cid=STORE-MSF77008-PS4ALLGAMESCATEG?emcid=pa-st-111690']
    
    #def __init__(self):#,
        #self.scraped_urls=['https://store.playstation.com/#!/en-us/all-ps4-games/cid=STORE-MSF77008-PS4ALLGAMESCATEG?emcid=pa-st-111690']
    
    #def start_requests(self):
    #    for url in start_urls:
    #        yield scrapy.Requests(url=url,callback=self.parse)
        
    def parse_product(self, response):
        yield load_product(response)

    #def parse(
 #       self, response
#        ):
