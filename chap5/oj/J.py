n = eval(input())
a = 0
g = 0
s = 0
b = 0
x = 1
for i in range(1, n + 1):
    a = i
    g = a % 10
    s = a // 10 % 10
    b = a // 100
    if i % 7 == 0 or g == 7 or s == 7 or b == 7:
        continue
    print("%4d" % i, end="")
    if (x % 15 == 0):
        print()
    x += 1
