students=['Michael', 'Bob', 'Tracy']

print(students)

print(len(students))

#append 追加一个元素
students.append('zs')
print(students)

print(len(students))

#insert在指定位置添加一个元素
students.insert(1,'ls')
print(students)

print(len(students))

#pop 删除列表的最后一个元素
students.pop()
print(students)
print(len(students))

#list 的元素可以是一个list
p = ['ww',students]
print(p)
print(p[1][0])
print(len(p))
