def add_end(L=[]):
    L.append('END')
    return L

def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# l=add_end([1, 2, 3])
i=5
while i>0:
    print(add_end1())
    i=i-1

