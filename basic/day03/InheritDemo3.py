# -*- coding: utf-8 -*-
# 隐藏属性
class People(object):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("error:名字长度需要大于或者等于5")

student = People("yy")
student.setName("xxxxxx")
print(student.getName())
