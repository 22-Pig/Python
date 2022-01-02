n = int(input())
num = -1
for i in range(n):
    if i <= n // 2:
        num = num + 2
    else:
        num = num - 2
    numk = (11 - num) // 2
    print(' ' * numk, end='')
    print('*' * num, end='')
    print(' ' * numk)