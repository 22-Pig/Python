try:
    n = float(input())
    s = input()
    m = float(input())
    if s[0] == '+':
        print("{:.2f}".format(n + m))
    elif s[0] == '-':
        print("{:.2f}".format(n - m))
    elif s[0] == '*':
        print("{:.2f}".format(n * m))
    elif s[0] == '/':
        print("{:.2f}".format(n / m))
except ZeroDivisionError:
    print("divided by zero")