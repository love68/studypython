#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

sendArr = ('127.0.0.1',8888)

#sendData = "1111"

sendData = input("请输入要发送的数据")

print("输入的数据尾%s"%sendData)

data = sendData.encode()


udpSocket.sendto(data,sendArr)

udpSocket.close()

