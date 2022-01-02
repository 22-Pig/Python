a = list(map(int, input().split(",")))
b = [6, 7, 8, 9, 10]
for i in set(a):
    if 6 <= i <= 10:
        if i in b:
            b.remove(i)
for i in b[0:-1]:
    print(i, end=" ")
print(b[-1])
