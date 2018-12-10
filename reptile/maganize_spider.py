#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: maganize_spider.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-08 20:14:05
############################

import urllib
import urllib.request
import re
from lxml import etree
import requests
import time
import pymysql

class Maganize(object):
    def __init__(self):
        pass

class MaganizeSpider(object):

    count = 0

    def __init__(self,endPage):
        self.__headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows     NT 6.1; Trident/5.0)"}
        self.__maganize = []
        self.endPage = endPage

    def getHeaders(self):
        return self.__headers

    def getMaganize(self):
        return self.__maganize

    def setMaganize(self,item):
        self.__maganize.append(item)

    def clearMaganize(self):
        self.__maganize=[]    

    def start(self):
        for i in range(self.endPage+1):
            self.loadPage(i)

    def loadPage(self,pageNum):
        #proxy_handler = urllib.request.ProxyHandler({"https":"112.67.37.243:8118"})

        #opener = urllib.request.build_opener(proxy_handler)

        url = "https://www.zazhi.com.cn/qikan/s0l0l0l0l0l0l0l0l0l02"+str(pageNum)+".html"
        #url = "http://wenshu.court.gov.cn/"

        #request = urllib.request.Request(url,headers=headers)

        #response = urllib.request.urlopen(request)
        
        response = requests.get(url,self.getHeaders())
        #print(response.encoding)#查看响应编码
        html = response.text
        self.getH4Content(html)

    def getH4Content(self,html):
        pattern = re.compile(r'<h4>(.*?)</h4>',re.S)
        h4s = re.findall(pattern,html)#获取到每一个h4标签的内容
        self.getUrl(h4s)

    def getUrl(self,h4s):
        '''
            获取每一个h4中的href
        '''
        #pattern = re.compile(r'href="(.*?)"',re.S)
        pattern = re.compile(r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')',re.S)
        pattern_title = re.compile(r'>(.*?)<',re.S)
        for h4 in h4s:
            url = re.search(pattern,h4).group(0)
            title = re.search(pattern_title,h4).group(0).replace('>','').replace('<','')
            #print(url.replace('//','').replace('/',''))#href="//
            url ="https://"+ url.replace('//','')[:-1]
            self.loadBookPage(url,title)

     
    def loadBookPage(self,url,title):
         '''
            加载杂志信息页
         '''
         time.sleep(1)
         response = requests.get(url,headers=self.getHeaders())
         html = response.text
         intro = etree.HTML(html).xpath('//div[@class="body-box"]//p')[0].text
         #print(intro)
         self.getBookInfo(html,title,intro)

    def getBookInfo(self,html,title,intro):
        #pattern = re.compile(r'<div class="item">(.*?)</div>',re.S)
        pattern = re.compile(r'<ul class="after-clear">(.*?)</ul>',re.S)
        content = re.search(pattern,html).group(0)
        pattern_intro = re.compile(r'<div class="con">(.*?)</div>',re.S)
        #intro = re.search(pattern_intro,html).group(0).replace('\n','').replace('<p>','').replace('</p>','').replace('</div>','')[17:300]
        #print(content)
        html_content = etree.HTML(content)

        p1=re.compile(r'<li>(.*?)</li>',re.S)

        lis = re.findall(p1,content)
        

        m = Maganize()
        m.title = title
        m.intro = intro
        m.mag_competent = ''
        m.mag_hostunit = ''
        m.mag_issn = ''
        m.mag_cn = ''
        m.mag_mailnum = ''
        #m.mag_addtime = ''
        m.mag_pubcycle = ''

        i = 0
        if len(lis)== 9:
            while i<len(lis):
                i += 1
                if i == 0:
                    m.mag_competent = html_content.xpath('//a')[0].text
                elif i==1:
                    m.mag_hostunit = html_content.xpath('//a')[1].text
                elif i==2:
                    m.mag_issn = lis[i][18:]
                elif i==3:
                    m.mag_cn = lis[i][18:]
                elif i== 5:
                    m.mag_mailnum =lis[i][18:]
                elif i==7:
                    m.mag_pubcycle = html_content.xpath('//a')[3].text
            self.insert(m)        
            #print(m.title,m.mag_competent,m.mag_hostunit,m.mag_mailnum,m.mag_issn,m.mag_cn,m.mag_pubcycle,m.intro)

        #print(html_content.xpath('//a')[0].text)
        #print(html_content.xpath('//a')[1].text)
        #print(html_content.xpath('//a')[2].text)
        #print(html_content.xpath('//a')[3].text)
        #print(html_content.xpath('//a')[7].text)
        
        '''
        if "主管单位："==html_content.xpath('//span')[0].text:
            m.mag_competent = html_content.xpath('//a')[0].text
        elif "主办单位："==html_content.xpath('//span')[1].text:
            m.mag_hostunit = html_content.xpath('//a')[1].text
        elif "国际刊号："==html_content.xpath('//span')[2].text:

            m.mag_issn = html_content.xpath('//a')[2].text
            print(html_content.xpath('//li')[2].text[10:-6])
        elif "国内刊号："==html_content.xpath('//span')[3].text:
            m.mag_cn = html_content.xpath('//a')[3].text
        elif "邮发代号："==html_content.xpath('//span')[5].text:
            m.mag_mailnum = html_content.xpath('//a')[5].text
        #elif "创刊时间："==html_content.xpath('//span')[6].text:
         #   m.mag_addtime = html_content.xpath('//a')[6]
        elif "发行周期："==html_content.xpath('//span')[7].text:
            m.mag_pubcycle = html_content.xpath('//a')[7].text
        else:
            pass
        '''
        #self.setMaganize(m)

        #if len(self.getMaganize()) == 10:
        #self.insert(m)

    def insert(self,m):
        try:
            conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="hasee",
                    database="test",charset="utf8")
            
            print("------starting--------------")
            print(m.title,m.mag_competent,m.mag_hostunit,m.mag_mailnum,m.mag_issn,m.mag_cn,m.mag_pubcycle,m.intro)
            cs1 = conn.cursor()
            
            print("正在插入第%d行数据"%self.count)
            sql = "insert into mag(mag_title,mag_competent,mag_hostunit,mag_mailnum,mag_issn,mag_cn,mag_pubcycle,mag_intro) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            self.count += cs1.execute(sql,(m.title,m.mag_competent,m.mag_hostunit,m.mag_mailnum,m.mag_issn,m.mag_cn,m.mag_pubcycle,m.intro))
            print("插入第%d行数据成功"%self.count)

            conn.commit()
            #self.clearMaganize()
            print("------over--------------")
            cs1.close()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    m = MaganizeSpider(5)
    m.start()
        


