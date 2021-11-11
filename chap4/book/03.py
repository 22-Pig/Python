n = int(input("请输入最大范围："))
list = []
for i in range(1, n + 1):
    for j in range(1, i):
        if i % j == 0:
            list.append(j)
    if sum(list) == i:
        print("{}是完数，其因子包括{}".format(i, list))
    list.clear()
