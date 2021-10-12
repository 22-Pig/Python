a, n = map(int, input().split())
num = 0
sum = 0
for i in range(1, n + 1):
    num = num * 10 + a
    sum += num
print("s =", sum)
