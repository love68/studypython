# -*- coding: utf-8 -*-
def add(x):
    return x+x


L = []
for i in range(2):
    L.append(i)
print(L)
# map第一个参数是函数，第二个是iterable，返回Iterator
s = map(add, [1, 2])
print(list(s))


