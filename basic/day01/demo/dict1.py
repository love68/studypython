d = {'a': 1, 'b': 2, 'c': 3}

# 迭代key
for key in d:
    print(key,end="")
    print(d.get(key))

# 迭代value
for value in d.values():
    print(value,end=""+" ")
print()
# 迭代key和value
for item in d.items():
    print(item,end="")

print()
print(d)
