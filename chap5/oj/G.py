n = eval(input())
a = []
b = []
for i in range(n):
    a.append(eval(input()))
for i in range(n):
    if a[i] % 2 != 0:
        b.append(a[i])
for i in b:
    print(i, end=' ')
print()
print(len(b))
