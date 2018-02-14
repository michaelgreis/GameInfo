# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os


class SteamInjestPipeline(object):
    def process_item(self, item, spider):
        line = dict(item)
        with open('/crawlerSteam/steam'+str(time.time())+'.json','w',encoding='utf-8') as outfile:
           outfile.write(str(dict(item)).replace("'",'"'))
        outfile.close()
        return item
