def fn(a, n):
    if n == 1:
        return a
    else:
        return eval(str(a) * n) + fn(a, n - 1)


a, b = input().split()
s = fn(int(a), int(b))
print(s)
