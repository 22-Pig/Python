from math import sqrt


def isPrime(p):
    if p == 1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


def PrimeSum(m, n):
    sum = 0
    for i in range(m, n + 1):
        if (isPrime(i)):
            sum += i
    return sum


m, n = input().split()
m = int(m)
n = int(n)
print(PrimeSum(m, n))
