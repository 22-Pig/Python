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
