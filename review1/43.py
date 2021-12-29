def gcd(a, b):

    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(smaller + 1):
        if a % (smaller - i) == 0 and b % (smaller - i) == 0:
            return smaller - i


def lcm(m, n):

    if m > n:
        greater = m
        smaller = n
    else:
        greater = n
        smaller = m
    i = 1
    while True:
        if greater * i % smaller == 0:
            return greater * i
        i += 1


x, y = map(int, input().split())
print('{:d} {:d}'.format(gcd(x, y), lcm(x, y)))
