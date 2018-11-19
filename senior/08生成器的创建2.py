#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#创建生成器的第二种方式，函数

def fib(n):
    a,b = 0,1
    i = 0
    while(i<n):
        a,b = b,a+b
        #print(a)
        yield a
        i += 1

if __name__ == "__main__":
   g = fib(5)
   print(g)
   #for temp in g:
   #    print(temp)
   
   while True:
       try:
           print(next(g))
       except StopIteration as e:
           print("%s"%e)
           break





