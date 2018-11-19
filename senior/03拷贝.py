# copy
import copy
a = [1,2,3]
b = copy.copy(a)


print("a=%s"%a)
print("b=%s"%b)
print(a is b) #False

a.append(4)

print("a=%s"%a)
print("b=%s"%b)
print(a is b) #False
