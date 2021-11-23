a = map(int, input().split())
m = {}
for x in a:
    m[x] = m.get(x, 0) + 1
for k in m.keys():
    print(k, m.get(k, 0))
