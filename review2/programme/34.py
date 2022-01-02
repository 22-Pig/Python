a, b = map(int, input().split())
if a < 0 and b < 0:
    print('-_-')
elif a + b > 0:
    print(max(a, b), a + b)
    print('^_^')
elif a + b < 0:
    print(max(a, b), '0')
    print('T_T')