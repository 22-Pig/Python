m, n = map(int, input().split())
flag = 0
for i in range(m, n + 1):
    c = []
    a = []
    b = i
    while int(b) != 0:
        b = b / 2
        if int(b) == 0:
            break
        if a == []:
            b = int(b)
            if i % b == 0:
                a.append(b)
                continue
            else:
                break
        if b % int(b) == 0:
            a.append(int(b))
        else:
            b = int(b) + 1
            a.append(b)
        if i % int(b) != 0:
            break
    if i == sum(a):
        for j in range(1, i):
            if i % j == 0:
                if j not in c:
                    c.append(j)
        if set(c).symmetric_difference(set(a)) != set():
            continue
        flag += 1
        print(i, end='')
        print(' = {}'.format(a[(len(a) - 1)]), end='')
        for x in range(len(a) - 2, -1, -1):
            if x == 0:
                print(' + {}'.format(a[x]))
            else:
                print(' + {}'.format(a[x]), end='')
if flag == 0:
    print('None')
