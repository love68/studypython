
'''
不带参数的装饰器
'''

def w(func):
    def inner():
        print("1")
        func()
        print("2")
    return inner


@w
def test():
    print("---test---")


test()
        


