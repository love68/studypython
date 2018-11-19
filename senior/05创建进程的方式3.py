import os
from multiprocessing import Process

class MyProcess(Process):
    # 创建一个类继承Process
    def __init__(self,name):
        Process.__init__(self)
        self.__name = name

    # 重写run方法，调用start时，如果没有给Process的target
    # 传参，那么会默认调用run

    def run(self):
        print(self.name)
        print("我是子进程，进程号是%s,进程名是%s"%(os.getpid(),self.name))
        

if __name__ == "__main__":
    print("我是父进程，进程号是%s"%(os.getpid()))
    p = MyProcess("进程1")
    p.start()
    p.join()


