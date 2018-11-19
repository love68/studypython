import os

pid = os.fork()

if(pid == 0):
    print("我是子进程，进程号是%s"%(os.getpid()))
    print("我是子进程，我的父进程号是%s"%(os.getppid()))
else:
    print("我是父进程，进程号是%s"%(os.getpid()))

print("over")

