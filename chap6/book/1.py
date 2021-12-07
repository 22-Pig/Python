def fn(a, n):
    if n == 1:
        return a
    else:
        return eval(str(a) * n) + fn(a, n - 1)


s = fn(2, 3)
print(s)
