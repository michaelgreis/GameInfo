import scrapy
import os
import time as time

class SonyScraper(scrapy.Spider):
    name="sony_scraper"
    custom_settings={
        'DOWNLOAD_DELAY':'5',
    }
    start_urls=['https://store.playstation.com/#!/en-us/all-ps4-games/cid=STORE-MSF77008-PS4ALLGAMESCATEG?emcid=pa-st-111690']
    
    def __init__(self,
        #output_directory=None,
        #source_name=None,
        *args,**kwargs):
        # working on implementing: https://stackoverflow.com/questions/15611605/how-to-pass-a-user-defined-argument-in-scrapy-spider
        super(SonyScraper, self).__init__(*args, **kwargs)
        self.scraped_urls=['https://store.playstation.com/#!/en-us/all-ps4-games/cid=STORE-MSF77008-PS4ALLGAMESCATEG?emcid=pa-st-111690']
        #self.name='sony_scraper'
        #self.output_location=output_directory
        #self.source_name=source_name
        #print(output_directory)
    #scraped_urls=[]

    def parse(
        self, response
        ):
        #print(self.output_location)
        #os.chdir(self.output_location)
        game_values = []
        #SET_SELECTOR='.statsText'
        #number_of_pages='.statsText'
        #for stat in response.css(SET_SELECTOR):
        #    PAGE_SELECTOR='span ::text'
        #    yield {
        #        'pages':stat.css(PAGE_SELECTOR).extract_first(),
        #    }
        SET_SELECTOR='.cellGridGameStandard'
        for game in response.css(SET_SELECTOR):
            IMAGE_SELECTOR='img'
            BADGESALE_SELECTOR='.badge ::text'
            GAMETITLE_SELECTOR='.cellTitle ::text'
            game_values.append({
                'image':game.css(IMAGE_SELECTOR).xpath('@src').extract_first(),
                'badge_sale':game.css(BADGESALE_SELECTOR).extract_first(),
                'game_name':game.css(GAMETITLE_SELECTOR).extract_first(),
            })
        NEXTPAGE_SELECTOR='.headPgCtl .pageLink:not([class^="pageLink inactive notLast selected"]) ::attr(href)'# .navlinks a ::attr(href)'
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
                outfile.write(str(game_values))
        outfile.close()
        #print(self.scraped_urls)

