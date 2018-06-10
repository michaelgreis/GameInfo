# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os
import json

class SonyPipeline(object):
    def process_item(self, item, spider):
        line = dict(item)
        with open('/crawlerdata/sony/sony'+str(time.time())+'.json','w',encoding='utf-8') as outfile:
            outfile.write(json.dumps(line))
        return item
