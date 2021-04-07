#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: insert.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-05 13:07:26
############################
import pymysql

try:
    conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="hasee",
            database="test",charset="utf8")
    cs1 = conn.cursor()
    count = cs1.execute("insert into user values(1,'zz','1')")
    print("插入了%d行数据"%count)
    conn.commit()
    cs1.close()
except Exception as e:
    print(e)

