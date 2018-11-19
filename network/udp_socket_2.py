from socket import *

arr = ('127.0.0.1',8888)

s = socket(AF_INET,SOCK_DGRAM)

s.bind(arr)

while True:
    data,address=s.recvfrom(1024)
    print(data)
    print(address)
    s.sendto('222'.encode(),address)

s.close()
