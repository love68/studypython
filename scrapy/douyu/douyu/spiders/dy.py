# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem

class DySpider(scrapy.Spider):
    name = 'dy' # scrapy crawl dy 运行时的名字
    allowed_domains = ['douyu.com']#允许爬取的域
    start_urls = ['https://www.douyu.com/directory/all']#第一个要爬取的url

    def parse(self, response):
        #content = response.text
        roots = response.xpath('//div[@class="mes"]')
        for root in roots:
            item = DouyuItem()
            item['name']=root.xpath('.//h3/text()').extract()[0].replace(' ','')
            item["title"]=root.xpath('.//span/text()').extract()[0].replace(' ','')
            yield item


