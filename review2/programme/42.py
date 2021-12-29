import math

n = int(input())
for p in range(2, n):
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            break
    else:
        q = n - p
        for k in range(2, int(math.sqrt(q)) + 1):
            if q % k == 0:
                break
        else:
            print("{} = {} + {}".format(n, p, q))
            break
