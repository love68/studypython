#/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: proxyip.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-07 15:00:44
############################

import urllib
import urllib.request

proxy_handler = urllib.request.ProxyHandler({"https":"112.67.37.243:8118"})

opener = urllib.request.build_opener(proxy_handler)

headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

request = urllib.request.Request("http://wenshu.court.gov.cn/",headers=headers)

response = opener.open(request)

print(response.read().decode("utf-8"))
