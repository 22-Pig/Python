<<<<<<< HEAD
n = 0
for i in range(1, 501):
    if i % 3 == 0:
        n += 1
print(n)
=======
m, n = map(int, input().split())
s = []
l = []
for i in range(m):
    s.append([i for i in input().split()])
for j in range(n):
    for i in range(m):
        l.append(s[i][j])
    print(' '.join(l))
    l = []
>>>>>>> 4d0cc0186e62cea2072127df4b846abba88a58b9
