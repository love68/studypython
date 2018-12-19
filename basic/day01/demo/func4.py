# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3,4,2.1))

num = [1,2,3]
# list 作为可变参数
print(calc(*num))
