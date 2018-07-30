# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os
import json


class SteamInjestPipeline(object):
    def process_item(self, item, spider):
        line = dict(item)
        with open('/crawlerdata/steam/steam'+str(time.time())+'.json','w',encoding='utf-8') as outfile:
           #outfile.write('['+str(dict(item)).replace("{'",'{"').replace("'}",'"}').replace(",'",',"').replace("':",'":').replace(" '",' "').replace("',",'",').replace("['",'["').replace("']",'"]')+']')
           outfile.write(json.dumps(line))
        outfile.close()
        return item
