# -*- coding: utf-8 -*-
file = open("test.txt","r",encoding="utf-8")
# file.read(10)
# file.read(1)
# file.readlines()
# file.readlines()
# file.readlines()
# file.readlines()
# # 获取当前读到的位置
# print(file.tell())

while len(file.read(1024)) != 0:
    print(file.read(1024))

file.close
