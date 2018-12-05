#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: udp_client.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-04 19:39:27
############################
from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

address = ('192.168.1.111',6666)

data = input("请输入要发送的数据")

udpSocket.sendto(data.encode("utf-8"),address)

receData = udpSocket.recvfrom(1024)

print("发送的数据为%s,接收到的数据为%s"%(data,receData))

udpSocket.close()


