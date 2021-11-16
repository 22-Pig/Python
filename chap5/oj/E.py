n = int(input())
a, s = 1, 0
for i in range(1, n + 1):
    a = a * i
    s = s + a
print(float('%.1f' % s))
