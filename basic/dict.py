d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Tracy'])
print('bos' in d)

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
for n in d:
	print(n)
	print(d[n])
	print(d.get(n))