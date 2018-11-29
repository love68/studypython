from threading import Thread
import time

l = [1,2,3]

def test(l):
    l.append(4)
    print(l)

t1 = Thread(target=test,args=(l,))
t1.start()


t2 = Thread(target=test,args=(l,))
t2.start()


