#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: 07ThreadLocal的使用.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-11-29 15:50:02
############################

import threading

'''
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
'''



#创建一个ThreadLocal对象
local_school = threading.local()

def test():
    student_name = local_school.student_name
    print("线程名%s,学生名%s"%(threading.current_thread().name,student_name))


def hander(name):
    #绑定变量
    local_school.student_name = name
    test() 

t1 = threading.Thread(target=hander,name="线程1",args=("张三",))
t1.start()
t2 = threading.Thread(target=hander,name="线程2",args=("李四",))
t2.start()


