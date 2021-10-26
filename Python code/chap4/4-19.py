sum = 0
m,n = map(int, input().split())
if m==1:	#1不是素数
    m = 2
prime = []	#记录已知素数的列表
for x in range(2, n+1):
    isprime = True
    for k in prime:
        if x%k == 0:
            isprime = False
            break
    if isprime:
        if x >= m:
            sum += x
        prime.append(x)	#加入已知素数的列表，用于下一次计算
print(sum)






