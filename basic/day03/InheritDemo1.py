# -*- coding: utf-8 -*-
class base(object):
    def test(self):
        print("Base")


class A(base):
    def test(self):
        print("AAAA")


class B(base):
    def test(self):
        print("BBBB")

class C(B,A):
    def test(self):
        print("CCCC")

c = C()
c.test()


#可以查看C类的对象搜索方法时的先后顺序
print(C.__mro__)

