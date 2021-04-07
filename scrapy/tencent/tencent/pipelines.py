# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def __init__(self):
        self.file = open("position.json","w")


    def process_item(self, item, spider):
        position = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(position)
        return item
