a, n = map(int, input().split())
sum = 0
t = 0
for i in range(n):
    t = t * 10 + a
    sum = sum + t
print("s = {:d}".format(sum))
