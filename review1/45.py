import math


def issu(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


m = int(input())
for i in range(2, m):
    if issu(i) and issu(m - i):
        print("{} = {} + {}".format(m, i, m - i))
        break