#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import urllib.request

url = "https://movie.douban.com/top250?start=25&filter="


headers = {
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}


request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read())

