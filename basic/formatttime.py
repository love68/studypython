#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: formatttime.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-10 15:02:44
############################
import time

#格式化当前时间
#print(time.localtime())
'''
%Y：年(4位)
%y：年(2位)
%m：月
%d：日
%D：月/日/年
%H：时
%M：分
%S：秒
%w：星期
%W：本周是今年的第几周
'''
print(time.strftime("%Y%m%d",time.localtime()))
print(time.strftime("%Y%m%d %H:%M:%S",time.localtime()))
print(time.strftime("%D%w",time.localtime()))

