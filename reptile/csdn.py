#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: csdn.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-17 15:32:56
############################

import urllib
import requests

session = requests.Session()

url = "https://passport.csdn.net/v1/register/pc/login/doLogin"
headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"}

data={
        "loginType":"1",
        "pwdOrVerifyCode":"jiajunkang88888",
        "userIdentification": "jiajunkang@outlook.com"
}

url2 = "https://passport.csdn.net/v1/register/checkCaptchaSwitch?type=1&userIdentification=jiajunkang@outlook.com"

response = session.get(url2).text

print(response)

#data = urllib.parse.urlencode(data).encode("UTF-8")

reponse = session.post(url,data=data,headers=headers)

print(reponse.text)

