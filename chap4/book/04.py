m, n = map(int, input().split())
count = 0
s = 0
for num in range(m, n + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            count += 1
            s += num
print(count, s)
