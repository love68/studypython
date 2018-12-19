# -*- coding: utf-8 -*-
stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":19},
    {"name":"wangwu", "age":17}
]
#按名字排序
# stus.sort(key = lambda x:x['name'])

#按年龄排序
stus.sort(key = lambda x:x['age'])

print(stus)