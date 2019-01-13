# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
import re
from lxml import etree

class SpidertencentSpider(scrapy.Spider):
    name = 'spidertencent'
    allowed_domains = ['hr.tencent.com']
    url = "https://hr.tencent.com/position.php?start="
    pageNum = 0
    start_urls = [url+str(pageNum)]

    def parse(self, response):
        item = TencentItem()
        pattern1 = re.compile(r'<tr class="(even|odd)">(.*?)</tr>',re.S)
        #pattern2 = re.compile(r'<td(.*?)>(.*?)</td>',re.S)
        positions = re.findall(pattern1,response.text)
        for position in positions:
            # infos = re.findall(pattern2,position[1])
            # for info in infos:
            #     print(info[1])
            try:

                c = etree.HTML(position[1])
                item['name'] = c.xpath("//td/a/text()")[0]
                item['positiontype']=c.xpath("//td/text()")[0]
                item['num'] = c.xpath("//td/text()")[1]
                item['address'] = c.xpath("//td/text()")[2]
                item['positiontime'] = c.xpath("//td/text()")[3]
                yield item
            except Exception as e:
                print("")
                print(e)

        if self.pageNum < 2840:
            self.pageNum += 10
            yield scrapy.Request(self.url+str(self.pageNum),callback=self.parse)

        '''
        contents = response.xpath('//tr[@class="even" or @class="odd"]')
        for content in contents:
            #name = content.xpath('./td').extract()[0]
            name = content
            print(name)
            
            link = content.xpath('.//a/@href').extract()[0][:28] # 获取到每一个职位的连接
            fulllink = "https://hr.tencent.com/"+link
            yield scrapy.Request(fulllink,callback=self.parse_page)
            '''


    def parse_page(self,response):
        '''
            处理每一个页面，获取需要的信息
        '''
        infos = response.xpath()
            


