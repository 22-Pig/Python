n = int(input())
sum = 0
a = 1
b = 1
for i in range(n):
    if a % 2 == 0:
        sum -= a / b
    else:
        sum += a / b
    a += 1
    b += 2
print("%.3f" % sum)