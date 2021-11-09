i1 = int(input())
f = input()
i2 = int(input())
try:
    if f.__eq__('+'):
        res = i1 + i2
    elif f.__eq__('-'):
        res = i1 - i2
    elif f.__eq__('*'):
        res = i1 * i2
    else:
        res = i1 / i2
except ZeroDivisionError:
    print("divided by zero")
else:
    print('{:.2f}'.format(res))
