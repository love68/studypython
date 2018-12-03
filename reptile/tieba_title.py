#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: tieba_title.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-02 16:46:22
############################
import urllib
from lxml import etree
import requests

class TiebaSpider(object):
    
    def __init__(self):
        self.__page = 1

    def loadPage(self):
        url = "http://tieba.baidu.com/f?"
        data = {"kw":"美女","pn":"0"}
        data = urllib.parse.urlencode(data)

        url = url + data

        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        
        request = urllib.request.Request(url,headers=headers)
        html = urllib.request.urlopen(request).read()
        html = (html.decode("utf-8"))
        html_dom = etree.HTML(html)
        content = html_dom.xpath('//div[@class="threadlist_lz clearfix"]//a/@class')
        for item in content:
            print(item.text)

if __name__ == "__main__":
    tieba = TiebaSpider()
    tieba.loadPage()

