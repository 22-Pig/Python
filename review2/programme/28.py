a = dict(eval(input()))
b = dict(eval(input()))
<<<<<<< HEAD
for k in b.keys():
    a[k] = a.get(k, 0) + b[k]

t = list(a.items())
t.sort(key=lambda x: ord(x[0]) if type(x[0]) == str else x[0])
c = str(dict(t)).replace(' ', '').replace("'", '"')
print(c)
=======
for i in b:
    if i not in a:
        a[i] = b[i]
    else:
        a[i] += b[i]
print("{", end="")
s1 = [i for i in a.keys() if type(i) == type(1)]
s2 = [i for i in a.keys() if type(i) == type('a')]
s1.sort()
s2.sort()
c = 0
n = len(a)
for i in s1 + s2:
    c += 1
    if type(i) == type(1):
        print("{}:{}".format(i, a[i]), end='')
    else:
        print('"{}":{}'.format(i, a[i]), end='')
    if c != n:
        print(',', end='')
print("}")
>>>>>>> 4d0cc0186e62cea2072127df4b846abba88a58b9
