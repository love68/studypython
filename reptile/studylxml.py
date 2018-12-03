#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: studylxml.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-02 17:46:31
############################
from lxml import etree

def readHtmle():
    html = etree.parse("./hello.html")
    return html
#print(etree.tostring(html,pretty_print=True))

def getLis(html):
    lis = html.xpath("//li/@class")

    for li in lis:
        print(li)

def getA(html):
    hrefs = html.xpath('//li[@class="item-0"]/a/@href')
    for href in hrefs:
        print(href)


def getAcontent(html):
    '''
        获取a标签的内容
    '''
    contents = html.xpath('//li[@class="item-0"]/a')
    for content in contents:
        print(content.text)

def getTagName(html):
    '''
        获取标签名
    '''
    contents = html.xpath('//li//*[@class="bold"]')
    for con in contents:
        print(con.tag)



if __name__ == "__main__":
    html = readHtmle()
    #getA(html)
    #getAcontent(html)
    getTagName(html)

