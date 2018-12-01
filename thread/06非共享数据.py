#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: 06非共享数据.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-11-29 14:18:58
############################

from threading import Thread
import time

'''
 在多线程开发中，全局变量是多个线程都共享的数据，而局部变量等是各自线程的，是非共享的        
'''


class MyThread(Thread):

    def __init__(self,num,sleepTime):
        Thread.__init__(self)
        self.num = num
        self.sleepTime =sleepTime

    
    def run(self):
        self.num += 1
        time.sleep(self.sleepTime)
        print("线程%s,num = %d"%(self.name,self.num))


if __name__ == '__main__':
    t1 = MyThread(0,5)
    t1.start()
    t2 =MyThread(100,1)
    t2.start()





