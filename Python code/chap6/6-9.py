def f(a,l=[]):
    l.append(a)
    return l

l1=f(10)
l2=f(123,[1,2,3])
l3=f("b")
print(l1)
print(l2)
print(l3)
