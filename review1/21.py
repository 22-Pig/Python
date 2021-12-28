a = int(input())
sum = 0
n = 1
for i in range(a):
    sum += 1 / n
    n += 2
print("sum = %.6f" % sum)