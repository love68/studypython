# -*- coding: utf-8 -*-

# 单例模式


class Student(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        print("--"*10)



s1 = Student()
s2 = Student()
s3 = Student()


print(id(s1))
print(id(s2))

s1.age = 10
print(s2.age)
