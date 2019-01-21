#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: kugousong.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-16 17:27:43
############################
import requests

headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"}

url = "http://fs.w.kugou.com/201812161726/87e0ddc381f02970dba8456cc6919aa9/G114/M07/1F/04/sg0DAFlKHeeAIuuhAFKMQ0TqEYw721.mp3"

response = requests.get(url,headers=headers)

with open('kug.mp3',"wb") as f:
    f.write(response.content)

print("完成")


