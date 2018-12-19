#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，
#把该判断对应的语句执行后，就忽略掉剩下的elif和else
age=10
if age >7:
	print(age)
	print('ok')
elif age>8:
	print(age)
	print("xx")
else:
	print("xxxx")
