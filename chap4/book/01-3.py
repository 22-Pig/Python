line = 5
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
    print('')
