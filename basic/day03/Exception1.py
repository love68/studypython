# -*- coding: utf-8 -*-
class MyException(Exception):
    # 自定义异常
    def __init__(self,length,atleast):
        # super().__init__()
        """"
        这一行代码，可以调用也可以不调用，建议调用，因为__init__方法往往是用来对创建完的对象进行初始化工作，
        如果在子类中重写了父类的__init__方法，即意味着父类中的很多初始化工作没有做，这样就不保证程序的稳定了，
        所以在以后的开发中，如果重写了父类的__init__方法，最好是先调用父类的这个方法，然后再添加自己的功能
        """
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            # raise引发一个你定义的异常
            raise MyException(len(s), 3)
    except MyException as result: #这个变量被绑定到了错误的实例
        print('MyException: 输入的长度是 %d,长度至少应是 %d'% (result.length, result.atleast))
    else:
        print('没有异常发生.')

main()










