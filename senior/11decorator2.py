
'''
带参数的装饰器
'''

def w(func):
    def inner(a,b):
        print("装饰器执行之前")
        result = a + b
        print("a+b=%d"%result)
        func(a,b)
        print("装饰器执行之后")
    return inner


@w
def test(a,b):
    print("a=%d"%a)
    print("b=%d"%b)

test(1,2)



