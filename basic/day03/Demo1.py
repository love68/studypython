# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name):
        self.name = name
        self.__age = 0

    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return self.__age


student = Student("大头")
print(student.name)
student.set_age(30)
print(student.get_age())