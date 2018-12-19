# -*- coding: utf-8 -*-
import os
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print([x * x for x in range(1, 11)])

# for循环后面还可以加上if判断，可以筛选出仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])

# 列表生成式
print([d for d in os.listdir('.')])

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])
