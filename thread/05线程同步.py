#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: 05线程同步.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-11-27 14:16:57
############################

from threading import Thread,Lock
import time

num = 0
mutex = Lock()#创建一个互斥锁，默认未上锁

def test():
    global num
    for i in range(100000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            num += 1
            mutex.release()
    print("num=%d"%num)        
        

def test1():
    global num
    for i in range(100000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            num += 1
            mutex.release()

    print("num=%d"%num)        

t1 = Thread(target=test)
t1.start()

t2 = Thread(target=test)
t2.start()

print("num = %d"%num)






