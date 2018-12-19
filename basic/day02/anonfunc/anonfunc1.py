# -*- coding: utf-8 -*-

# 使用lambda创建匿名函数

""""
Lambda函数能接收任何数量的参数但只能返回一个表达式的值
匿名函数不能直接调用print，因为lambda需要一个表达式
"""

sum = lambda x, y: x + y

print(sum(1, 2))
