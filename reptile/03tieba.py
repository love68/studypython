#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: 03tieba.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-11-30 16:39:21
############################

import urllib
import re
import requests

url = "http://tieba.baidu.com/f?kw=python&pn=50&"

data = {"kw":"python","pn":"0"}
data = urllib.parse.urlencode(data)

url = url + data

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

def loadPage(page):
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    return response.read().decode("utf-8")

def handleContent(content):
    pattern = re.compile(r'<a rel="noreferrer" href=".*?" title=".*?".*?>(.*?)</a>',re.S)
    #print(content)
    content_list = pattern.findall(content)
    for item in content_list:
        print(item)


if __name__ == "__main__":
    content = loadPage(1)
    handleContent(content)

