# -*- coding: utf-8 -*-
class Person:
    # 设置默认的属性值，类似构造函数
    def __init__(self, name='xxx', age="22"):
        self.name = name
        self.age = age

    # 类似toString方法
    def __str__(self):
        return "name = " + self.name + "\t" + ",age = " + self.age

    # 普通方法
    def study(self):
        print("学习Python")


""""
person = Person()
person.age = 23
print(person.age)
print(person.study())
"""
person = Person()
print(person.age)
print(person.study())
print(person)

person1 = Person("jjjk", '10')
print(person1.age)
print(person1)
