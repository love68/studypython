#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: findall.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-02 14:10:43
############################
import re

content = '<div class="threadlist_title pull_left j_th_tit ">
    
        
            <a rel="noreferrer" href="/p/5966738037" title="资料免费送，需要的留言" target="_blank" class="j_th_tit ">资料免费送，需要的留言</a>
            </div>'

pattern = re.compile(r'<a.*?">(.*?)</div>',re.S)

for ime in pattern.findall(content):
    print(ime)



