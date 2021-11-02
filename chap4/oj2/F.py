n = eval(input())
f = 1
for i in range(1, n + 1):
    print("%4d" % (f * i), end='')
    f = -f
