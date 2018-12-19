def power(x,n=2):
    s = 0
    while n>0:
        s = x*x
        n=n-1
    return s

s = power(5,2)

print('5的平方%d' % s)
print('5的平方%d' % power(5))


