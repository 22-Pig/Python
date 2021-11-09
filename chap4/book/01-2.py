line = 5
for i in range(1, line + 1):
    space = line - i
    for s in range(1, space + 1):
        print(' ', end='')
    star = 2 * i - 1
    for t in range(1, star + 1):
        print('*', end='')
    print('')
