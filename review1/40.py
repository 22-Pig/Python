a = 1
sum = 1
n = int(input())
for i in range(1, n + 1):
    a *= i
    item = 1 / a
    sum += item
print("{:.8f}".format(sum))