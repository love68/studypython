#tuple 是不可变得
tuple1 = (1,)
print(tuple1)

st = ['ls','zs']
tuple1 = ('ww',st)
print(tuple1)
print(len(tuple1))

st.append('mz');
print(tuple1)


