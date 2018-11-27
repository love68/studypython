#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import urllib
import requests

#如果使用urllib.parse.urlencode必须引入requests

url = "https://www.baidu.com/s"

word = {"wd":"中国"}
word = urllib.parse.urlencode(word)
#word = urllib.parse.urlencode(word)

url = url + "?" + word

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
response = urllib.request.Request(url=url,headers=headers)

html = urllib.request.urlopen(response)

html = html.read()
'''
f = open("search.html","wb+")

f.write(html)

f.close()
'''
with open("search.html","wb+") as f:
    f.write(html)

    

