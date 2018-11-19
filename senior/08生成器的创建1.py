#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#创建生成器的第一种方式，将列表生成式的中括号换成小括号

l = [x*2 for x in range(5) ]
print(l)

g = (x*2 for x in range(5))

print(g)

print(next(g))
