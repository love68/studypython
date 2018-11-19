import os

num = 1

pid = os.fork()

if(pid == 0):
    num = 100
    print("子进程num=%d"%num)
else:
    num = 200
    print("父进程num=%d"%num)

print(num)
    
