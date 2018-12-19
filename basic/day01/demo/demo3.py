# -*- coding: utf-8 -*-
from collections import Iterable
# 判断对象是否可循环
print(isinstance('abc',Iterable))

# 带下标循环
for i,value in enumerate([1,2,3]):
    print(i,value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
     print(x, y)