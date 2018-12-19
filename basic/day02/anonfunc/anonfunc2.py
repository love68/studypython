# -*- coding: utf-8 -*-

# 定义匿名函数
sum = lambda x, y: x + y


#
def test_anon(x, y, opt):
    print(x)
    print(y)
    print("result = %d " % opt(x, y))


# 匿名函数被当作实参调用
test_anon(1, 2, sum)
