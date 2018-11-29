from threading import Thread
import time

num = 0

def add():
	global num
	for i in range(100000):
		num +=1


t1 = Thread(target=add)
t1.start()



t2 = Thread(target=add)
t2.start()

print("num=%d"%num)
