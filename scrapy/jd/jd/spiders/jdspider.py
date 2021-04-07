# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem

class JdspiderSpider(scrapy.Spider):
    name = 'jdspider'
    allowed_domains = ['jd.com']
    page = 1
    url = 'https://search.jd.com/Search?keyword=java&page='
    start_urls = [url+str(page)]
    
    flag = "每满100-50"

    def parse(self, response):

        contents = response.xpath('//div[@id="J_goodsList"]//li[@class="gl-item"]')
        #contents = response.xpath('//i[@class="goods-icons4 J-picon-tips"]/text()')
        for content in contents:
            item = JdItem()
            #r = content.extract()
            eachs = content.xpath('.//i[@class="goods-icons4 J-picon-tips"]/text()')
            for each in eachs:
                result = each.extract()
                if result == self.flag:
                    item['price'] = content.xpath('.//div[@class="p-price"]//i/text()').extract()[0]
                    name_pre = content.xpath('.//div[@class="p-name"]//font/text()').extract()
                    if len(name_pre)>0:
                        name_pre = name_pre[0]
                        item['name'] =name_pre+ content.xpath('.//div[@class="p-name p-name-type-2"]//em/text()').extract()[0]
                    else:
                        item['name'] = content.xpath('.//div[@class="p-name p-name-type-2"]//em/text()').extract()[0]
                    yield item

        if self.page < 200:
           self.page += 1
           yield scrapy.Request(self.url+str(self.page),callback=self.parse)
            

                 


