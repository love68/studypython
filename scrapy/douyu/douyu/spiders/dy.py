# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem
#from bs4 import BeautifulSoup as bs
import json

class DySpider(scrapy.Spider):
    name = 'dy' # scrapy crawl dy 运行时的名字
    allowed_domains = ['douyu.com']#允许爬取的域
    offset = 1
    url = 'https://www.douyu.com/gapi/rkc/directory/0_0/'
    start_urls = [url+str(offset)]#第一个要爬取的url

    def parse(self, response):
        '''
        roots = response.xpath('//div[@class="mes"]')
        for root in roots:
            item = DouyuItem()
            item['title']=root.xpath('.//h3/text()').extract()[0].replace(' ','').replace("\r\n","")
            item["mold"]=root.xpath('.//span[@class="tag ellipsis"]/text()').extract()[0].replace(' ','')
            item["name"]=root.xpath('.//span[@class="dy-name ellipsis fl"]/text()').extract()[0].replace(' ','').replace("\r\n","")
            yield item
        '''
        content = response.text
        contents = json.loads(content)["data"]["rl"] # 将字符串转换为python对象
        for content in contents:
            item = DouyuItem()
            item['title'] = content['rn']
            item['mold'] = content['c2name']
            item['name']=content['nn']
            item['num']=content['ol']
            yield item


        if self.offset < 130:
            self.offset += 1
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
         


