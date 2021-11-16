b, c = map(eval, input().split())
a = 0
list = []
for x in range(10000000):
    if x < 2:
        continue
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        a += 1
        if b <= a <= c:
            list.append(x)
        elif a > c:
            break
s = sum(list)
print(s)
