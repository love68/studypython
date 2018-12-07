#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: doubantushu.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-05 18:48:49
############################
import urllib
import urllib.request
import re
import time
from lxml import etree

class Douban(object):

    def __init__(self,page):
        self._page = page

    def loadPage(self):
        url = "https://www.douban.com/doulist/1264675/?start=0"
        headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        
        request = urllib.request.Request(url,headers=headers)
        
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        self.parseHtml(html)
        

    def parseHtml(self,html):
        pattern = re.compile(r'<div class="title">(.*?)</div>',re.S)
        hrefs = re.findall(pattern,html)
        for href in hrefs:
            self.getUrl(href)
    
    def getUrl(self,href):
        pattern=re.compile(r'https://book.douban.com/subject/.*?/',re.S)
        myhref = re.search(pattern,href)
        self.getBookInfoPage(myhref.group(0))    
    
    def getBookInfoPage(self,url):
        headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows     NT 6.1; Trident/5.0)"}
        request = urllib.request.Request(url,headers=headers)
        html = urllib.request.urlopen(request).read().decode("utf-8")
        #self.getBookInfo(html)
        self.getBookContent(html)
    
    def getBookContent(self,html):
        htmldom = etree.HTML(html)
        title = htmldom.xpath('//div[@id="wrapper"]//h1/span').text
        print(title)



if __name__ == "__main__":
    d = Douban(1)
    d.loadPage()



