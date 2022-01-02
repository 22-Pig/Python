m = int(input())
for i in range(m):
    n = int(input())
    x = 2
    # 从2开始到n的平方根，枚举每个自然数x
    while x <= n // x:
        # x是n的因子
        if n % x == 0:
            print(str(x) + "*", end="")
            n //= x
        else:
            x += 1

    print(n)
