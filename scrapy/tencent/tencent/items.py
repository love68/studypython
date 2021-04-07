# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    positiontype = scrapy.Field()
    num = scrapy.Field()
    address = scrapy.Field()
    positiontime = scrapy.Field()
