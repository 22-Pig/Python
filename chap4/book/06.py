i1 = int(input())
f = input()
i2 = int(input())
try:
    if f == '+':
        result = i1 + i2
    elif f == '-':
        result = i1 - i2
    elif f == '*':
        result = i1 * i2
    else:
        result = i1 / i2
except ZeroDivisionError:
    print("divided by zero")
else:
    print('{:.2f}'.format(result))
