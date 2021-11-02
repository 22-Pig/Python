n = eval(input())
x = 1
for i in range(1, n + 1):
    print("%4d" % x, end='')
    x = -x
