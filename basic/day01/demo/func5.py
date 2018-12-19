# -*- coding: utf-8 -*-
def test(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


test(1, 2, 3, 4, 5, name="jjk", age=20)

A = (3, 4, 5)
B = {"name": "jjk", "age": 20}
test(1, 2, A, B)

test(1, 2, *A, **B)

