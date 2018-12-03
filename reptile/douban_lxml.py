#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: douban_lxml.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-02 18:29:56
############################
import urllib
from lxml import etree
import requests

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}


url = 'https://movie.douban.com/subject/27615441/'

request = urllib.request.Request(url,headers=headers)

res = urllib.request.urlopen(request)

html = etree.HTML(res.read().decode("utf-8"))

contents = html.xpath('//div[@class="info"]//a')

for c in contents:
    print(c.text)


