# -*- coding: utf-8 -*-
file = open("文件", "r+", encoding="utf8")
print(file.tell())
print(file.read(3))
file.write("hello")

# print(file)
# for line in file:
#     print(line.strip())
