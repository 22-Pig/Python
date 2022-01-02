<<<<<<< HEAD
a, b = map(int, input().split())
if a < 0 and b < 0:
    print('-_-')
elif a + b > 0:
    print(max(a, b), a + b)
    print('^_^')
elif a + b < 0:
    print(max(a, b), '0')
    print('T_T')
=======
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(str(j) + '*' + str(i) + '=', end='')
        print('{:<4d}'.format(i * j), end='')
    print()
>>>>>>> 4d0cc0186e62cea2072127df4b846abba88a58b9
