import math


def fun(eps):
    suma = 0
    count = 1
    c = 1
    while count > eps:
        count = 1 / math.pow(c, 2)
        suma += count
        c += 1
    return math.sqrt(suma * 6)


m = float(input())
print("{:.6f}".format(fun(m)))