x = list(input())
a = int(x[0])
b = int(x[1])
c = int(x[2])
if c == 0:
    if b == 0:
        print(a)
    else:
        print("%d%d" % (b, a))
else:
    print("%d%d%d" % (c, b, a))