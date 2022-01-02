a = input()
b = list(map(int, input().split()))
c = {}
b.sort()
for i in b:
    if i not in c:
        c[i] = 1
    else:
        c[i] += 1
sorted(c)
for i in c.keys():
    print(i, end=":")
    print(c[i])
