a, b = map(eval, input().split())
sum = 0
for i in range(a, b + 1):
    sum = sum + i * i + 1 / i
print("sum = {:.6f}".format(sum))