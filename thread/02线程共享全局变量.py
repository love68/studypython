#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from threading import Thread
import time

num = 1

def add():
    global num
    for i in range(100):
        num += 1


t1 = Thread(target=add)

t1.start()

time.sleep(2)

print("num = %d"%num)

t2 = Thread(target=add)
t2.start()

print("num = %d"%num)


