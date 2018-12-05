#!/usr/bin/python3
#-*- coding:utf-8 -*-
############################
#File Name: udp_server.py
#Author: jiajunkang
#Mail: jiajunkang@outlook.com
#Created Time: 2018-12-04 19:32:49
############################

from socket import *

address = ('',6666)

udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(address)

count = 0
while True:

    recvData = udp_socket.recvfrom(1024)

    udp_socket.sendto(recvData[0],recvData[1])

    print("接收到的消息是%s"%recvData[0])



