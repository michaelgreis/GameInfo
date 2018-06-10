# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader import ItemLoader

class SonyItem(scrapy.Item):
    image = scrapy.Field()
    badge_sale = scrapy.Field()
    game_name = scrapy.Field()
    plus_sale = scrapy.Field()
    console_type = scrapy.Field()
    item_type = scrapy.Field()

class SonyItemLoader(ItemLoader):
    default_output_processor = scrapy.loader.processors.Compose(scrapy.loader.processors.TakeFirst())