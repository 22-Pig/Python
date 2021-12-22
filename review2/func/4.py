pre = {0: 1, 1: 1}


def fib(n):
    if n in pre:
        return pre[n]
    else:
        newValue = fib(n - 1) + fib(n - 2)
        pre[n] = newValue
        return newValue


def PrintFN(m, n):
    lst = []
    i = 0
    while fib(i) <= n:
        if fib(i) >= m:
            lst.append(fib(i))
        i += 1
    return lst


m, n, i = input().split()
n = int(n)
m = int(m)
i = int(i)
b = fib(i)
print("fib({0}) = {1}".format(i, b))
fiblist = PrintFN(m, n)
print(len(fiblist))
