#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: thread_queue.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-07 17:18:43
############################

from queue import Queue
from threading import Thread,Lock,current_thread
import time
q = Queue()

for i in range(10000):
    q.put(i)

print(q.empty())

lock = Lock()

def printQueue():
    while True:    
        mutexFlag = lock.acquire(True)
        if mutexFlag:
            print("%s,%d"%(current_thread(),q.get()))
            lock.release()

def printQueue1():
    '''
        错误写法，其他线程没有执行机会
    '''
    mutexFlag = lock.acquire(True)
    while True:    
        if mutexFlag:
            time.sleep(1)
            print(q.get())
            lock.release()

t1 = Thread(target=printQueue)
t1.start()

t2 = Thread(target=printQueue)
t2.start()


    

