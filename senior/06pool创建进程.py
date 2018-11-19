from multiprocessing import Pool
import os
import time

def test():
    print("我是子进程，进程号是%s"%(os.getpid()))
    time.sleep(2)

p = Pool(3)

for i in range(0,20):
    p.apply_async(test)

print("----start---")
p.close()
p.join()
print("----start---")



