# -*- coding: utf-8 -*-
read_file = open("file1.py", "r", encoding='utf-8')

if read_file:
    print("文件已经打开")

write_file = open("copyfile1.py", "w", encoding='utf-8')

for temp in read_file.readlines():
    write_file.writelines(temp)

print("文件已经复制完毕")

read_file.close
write_file.close
