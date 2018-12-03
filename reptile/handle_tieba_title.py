#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: handle_tieba_title.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-02 18:05:57
############################
from lxml import etree

html = etree.parse("./title.html")


contents = html.xpath("//meta")

for content in contents:
    print(content.text)

