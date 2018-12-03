#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: match.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-02 12:53:57
############################

import re

pattern = re.compile("\d+")

s = "1l34"

m = pattern.match(s)

print(m.group())
