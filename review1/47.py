import math


def isPrime(p):
    if p == 1:
        return False
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


n = int(input())
while n > 0:
    num = int(input())
    if isPrime(num):
        print("Yes")
    else:
        print("No")
    n -= 1
