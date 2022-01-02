<<<<<<< HEAD
x = list(map(eval, input().split()))
# 将输入的9个数字转换成3*3的矩阵
a = []
b = []
c = []
d = []
for i in range(9):
    if 0 <= i <= 2:
        a.append(x[i])
    elif 3 <= i <= 5:
        b.append(x[i])
    elif 6 <= i <= 8:
        c.append(x[i])
d.append(a)
d.append(b)
d.append(c)

# 取出每行、每列及对角线和的最大值
hsum1 = 0
for i in range(3):
    hsum = 0
    for j in range(3):
        hsum += d[i][j]
    if hsum > hsum1:
        hsum1 = hsum

lsum1 = 0
for i in range(3):
    lsum = 0
    for j in range(3):
        lsum += d[j][i]
    if lsum > lsum1:
        lsum1 = lsum

zdsum1 = 0
for i in range(3):
    zdsum1 += d[i][i]

fdsum1 = 0
for i in range(3):
    fdsum1 += d[i][2 - i]

# 判断：
maxsum = []
maxsum.append(hsum1)
maxsum.append(lsum1)
maxsum.append(zdsum1)
maxsum.append(fdsum1)
print(max(maxsum))
=======
num = list(map(int, input().split()))
l = []
l.append(num[0] + num[4] + num[8])
l.append(num[2] + num[4] + num[6])
for i in range(0, 6, 3):
    l.append(num[i] + num[i + 1] + num[i + 2])
for j in range(0, 3, 1):
    l.append(num[j] + num[j + 3] + num[j + 6])
print(max(l))
>>>>>>> 4d0cc0186e62cea2072127df4b846abba88a58b9
