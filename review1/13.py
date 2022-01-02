from math import sqrt

m, n = map(int, input().split())

prime = []


def isPrime(p):
    if p == 1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


for i in range(m, n + 1):
    if (isPrime(i)):
        prime.append(i)

count = 1
suma = 0
c = 0
for i in prime:
    if i > m:
        c += 1
        suma += i
        print(i, end=' ')
        if count % 5 == 0:
            print()
            count = 0
        count += 1
if count % 5 != 0:
    print()
print("amount=%d sum=%d" % (c, suma))
