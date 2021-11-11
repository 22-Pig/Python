m, n = map(int, input().split())
sum = 0
if m > n:
    m, n = n, m
for i in range(m, n + 1):
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                pass
        else:
            sum += i
if sum == 0:
    print('not have prime!')
else:
    print(sum)
