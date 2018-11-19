from multiprocessing import Process
import os

def test(name):
    print(name)
    print("我是子进程，进程号是%s"%(os.getpid()))

if __name__ == '__main__':
    print("我是父进程，进程号是%s"%(os.getpid()))
    
    p=Process(target=test,args=("test1",))
    p.start()
    p.join() #父进程阻塞，等待子进程执行完毕
    

