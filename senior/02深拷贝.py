# python中的深拷贝
import copy

def printData(l):
    for temp in l:
        for t in temp:
            print(t,end="")

a = [1,2,3]
b = copy.deepcopy(a)

c = [a,b] # list and tuple have same result
d = copy.deepcopy(c)

print()
print("a=%s"%a) #a=[1, 2, 3]
print("b=%s"%b) #b=[1, 2, 3]
print(c) #([1, 2, 3], [1, 2, 3])
print(d) #([1, 2, 3], [1, 2, 3])

print(id(a)) #139703147615624
print(id(b)) #140407092102728

print("*"*30)

a.append(4)


print("a=%s"%a) #a=[1, 2, 3, 4]
print("b=%s"%b) #b = [1, 2, 3]
print(c) # ([1, 2, 3, 4], [1, 2, 3])
print(d) # ([1, 2, 3], [1, 2, 3])



