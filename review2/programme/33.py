num = int(input())
s = []
for i in range(num):
    s1, s2 = 0, 0
    count = int(input())
    for i in range(count):
        n = input()
        s.append([int(i) for i in n.split()])
    for index_h in range(count):
        for index_l in range(count):
            if index_l > index_h:
                s1 += s[index_h][index_l]
            elif index_l < index_h:
                s2 += s[index_h][index_l]
    if s1 == 0 and s2 != 0:
        print("lower triangular matrix")
    elif s1 != 0 and s2 == 0:
        print("upper triangular matrix")
    else:
        print("no")
    s = []
