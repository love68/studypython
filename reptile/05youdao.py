#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
#import os
#os.sys.path.append('/usr/local/lib/python3.7/site-packages')

import requests

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

word = input("请输入要翻译的单词")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=dict&smartresult=rule"

formdata = {
	'i': word,
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': 'dict',
                'client': 'fanyideskweb',
                'salt': '1523323753717',
                'sign': 'e9243107c4256bef73cd95bef15006e0',
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'action': 'FY_BY_CL1CKBUTTON',
                'typoResult': 'true'
}

formdata = urllib.parse.urlencode(formdata).encode(encoding='utf-8')

print(formdata)

request = urllib.request.Request(url,data = formdata,headers = headers)

response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))
