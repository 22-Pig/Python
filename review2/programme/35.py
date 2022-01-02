m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

t = False
for i in range(1, m - 1):  # 不循环边缘元素
    for j in range(1, n - 1):
        data = []  # 存储四周的四个值
        data.append(int(a[i - 1][j]))
        data.append(int(a[i + 1][j]))
        data.append(int(a[i][j - 1]))
        data.append(int(a[i][j + 1]))
        if a[i][j] > max(data):
            print(a[i][j], i + 1, j + 1)
            t = True
if t == False:
    print("None", m, n)
