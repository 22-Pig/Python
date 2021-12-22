""" line = int(input())
lineUp = int((line + 1) / 2)
lineDown = line // 2
for i in range(1, lineUp + 1):
    space = lineUp - i
    for s in range(1, space + 1):
        print(' ', end='')
    star = 2 * i - 1
    for t in range(1, star + 1):
        print('*', end='')
    print('')
for i in range(1, lineDown + 1):
    for s1 in range(1, i + 1):
        print(' ', end='')
    star1 = 2 * (lineDown - i) + 1
    for t in range(1, star1 + 1):
        print('*', end='')
    print('') """

n = int(input())
num = int(n / 2)
a = 5
for i in range(0, num):
    print(' ' * (a - i - 1), '*' * (i * 2 + 1), ' ' * (a - i - 1))
if num == 5:
    print('*' * 11)
    num = num - 1 
for i in range(num, -1, -1):
    print(' ' * (a - i - 1), '*' * (i * 2 + 1), ' ' * (a - i - 1))
