sum = 0
count = 0
m, n = map(int, input().split())
if m == 1:
    m += 1
for i in range(m, n + 1):
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        sum = sum + i
        count += 1
print("{:d} {:d}".format(count, sum))
