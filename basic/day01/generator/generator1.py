# -*- coding: utf-8 -*-
# 创建生成式的第一种方法
# 只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(g)

for n in g:
    print(n,end=""+"\t")
