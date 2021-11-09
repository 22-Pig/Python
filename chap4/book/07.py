m, n = map(int, input().split())
a = []
for i in range(m):
    s = input()
    a.append([int(n) for n in s.split()])
for j in range(m):
    sum = 0
    for k in range(n):
        sum += a[j][k]
    print(sum)
