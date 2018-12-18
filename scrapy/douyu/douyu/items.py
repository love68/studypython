# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()#姓名
    title =scrapy.Field()#标题
    mold = scrapy.Field()#类型
    num = scrapy.Field()#
    
