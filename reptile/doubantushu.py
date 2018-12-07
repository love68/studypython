#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: doubantushu.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-05 18:48:49
############################
import urllib
import urllib.request
import re
import time
from lxml import etree
from html.parser import HTMLParser
import pymysql

class Book(object):

    def __init__(self):
        pass



class Douban(object):

    def __init__(self,page):
        self._page = page

    def loadPage(self):
        url = "https://www.douban.com/doulist/1264675/?start=125"
        headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        
        request = urllib.request.Request(url,headers=headers)
        
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        self.parseHtml(html)
        

    def parseHtml(self,html):
        pattern = re.compile(r'<div class="title">(.*?)</div>',re.S)
        hrefs = re.findall(pattern,html)
        for href in hrefs:
            self.getUrl(href)
    
    def getUrl(self,href):
        pattern=re.compile(r'https://book.douban.com/subject/.*?/',re.S)
        myhref = re.search(pattern,href)
        self.getBookInfoPage(myhref.group(0))    
    
    def getBookInfoPage(self,url):
        headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows     NT 6.1; Trident/5.0)"}
        request = urllib.request.Request(url,headers=headers)
        html = urllib.request.urlopen(request).read().decode("utf-8")
        #self.getBookInfo(html)
        self.getBookContent(html)
    
    def getBookContent(self,html):
        book = Book()
        pattern1 = re.compile(r'<div class="intro">(.*?)</div>',re.S)
        book.book_summary = re.findall(pattern1,html)[0].replace('<p>','').replace('</p>','').replace('\n','')[:-70][:300]
    
        htmldom = etree.HTML(html)
        
        
        contents = htmldom.xpath('//div[@id="wrapper"]//div[@id="content"]//div[@id="info"]')
        info = etree.tostring(contents[0])
        pattern = re.compile(r'<span.*?>(.*?)<br/>',re.S)
        
        cs = re.findall(pattern,info.decode("utf-8"))
        
        book_name = htmldom.xpath('//div[@id="wrapper"]//h1/span')[0].text
        book_author = htmldom.xpath('//div[@id="wrapper"]//div[@id="info"]/a')
        #book_summary = htmldom.xpath('//div[@class="indent"]//div[@class="intro"]')[0].text.replace('<p>','').replace('</p>','').replace('\n','')
        if len(book_author) <= 0:
            book.book_author = ""
        else:
            book.book_author=book_author[0].text.replace(' ','').replace('\n','')
        book.book_name = book_name
        
        for c in cs:
            b = HTMLParser().unescape(c)
            p1 = re.compile(r'^.*?:</span>.*?$',re.S)
            ss = re.findall(p1,b)
            for s in ss:
                time.sleep(1)
                if s.split(":</span>")[0] == '出版社':
                    book.book_publish = s.split(":</span>")[1].replace(' ','')
                elif s.split(":</span>")[0] == '出版年':
                    book.book_pubtime = s.split(":</span>")[1].replace(' ','')
                elif s.split(":</span>")[0] == '页数':
                    book.book_numberpage = s.split(":</span>")[1].replace(' ','')
                elif s.split(":</span>")[0] == 'ISBN':
                    book.isbn = s.split(":</span>")[1].replace(' ','')
            
        #print(book.book_name,book.book_author,book.book_publish,book.book_summary,book.book_pubtime,book.book_numberpage,book.isbn)

        self.insertData(book)
        

    def insertData(self,book):
        '''
            
        '''
        try:
            conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="hasee",
                    database="test",charset="utf8")
            count = 0
            print("------starting--------------")

            cs1 = conn.cursor()
            
            sql = "insert into book(book_name,book_author,book_publish,book_pubtime,book_numberpage,isbn,book_summary) values(%s,%s,%s,%s,%s,%s,%s)"
            count += cs1.execute(sql,(book.book_name,book.book_author,book.book_publish,book.book_pubtime,book.book_numberpage,book.isbn,book.book_summary))
            print("插入了%d行数据"%count)
            conn.commit()
            print("------over--------------")
            cs1.close()
        except Exception as e:
            print(e)



if __name__ == "__main__":
    d = Douban(1)
    d.loadPage()



