# -*- coding: utf-8 -*-
path = "map.txt"
file = open(path,'r');

# 一次读取指定的字符
print(file.read(10))

# 一次读取一行数据
print(file.readline())

# file.readlines()，返回一个行数据的数组
for temp in file.readlines():
    print(temp)

# 一次读取所有数据
print(file.read())

file.close
