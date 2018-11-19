

'''
python的闭包:在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
'''


def test_out(numout):
    print("外部的变量%d"%numout)
    def test_in(numin):
        print("外部的变量%d"%numout)
        total = numin + numout
        print("内部外部变量之和%d"%total)
    return test_in


bibao = test_out(20)

bibao(10)


