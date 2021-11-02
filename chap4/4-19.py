sum = 0
m, n = map(int, input().split())
# 1不是素数
if m == 1:
    m = 2
# 记录已知素数的列表
prime = []
for x in range(2, n + 1):
    isprime = True
    for k in prime:
        if x % k == 0:
            isprime = False
            break
    if isprime:
        if x >= m:
            sum += x
# 加入已知素数的列表，用于下一次计算
        prime.append(x)
print(sum)
