# -*- coding: utf-8 -*-
class Father(object):
    def __init__(self,name,age):
        print("父类的init方法被调用了")
        self.name = name
        self.age = age

    def __str__(self):
        print("父类的str方法被调用了")
        msg = "name = " + self.name + "\t age = " + self.age
        return msg

    def my_print(self):
        print("father")


class Son(Father):

    def __init__(self,name,age):
        super().__init__(name,age)


f = Father("大明", "32")
print(f)

s = Son("小明", "12")
print(s.my_print())
print(s)









