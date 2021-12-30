n = int(input())
lst1 = []
lst2 = []
cnt = 0
for i in range(n):  # 创建一个二维列表
    lst1.extend(list(map(int, input().split())))
    lst2.append(lst1)
    lst1 = []
for i in range(n):
    for j in range(n):  # 遍历每一个列表元素
        if lst2[i][j] == max(lst2[i]):  # 如果这个元素在该行最大
            for k in range(n):  # 判断是否在该列为最小
                if lst2[i][j] >= lst2[k][j] and i != k:  # 如果在该列有更小的数，break
                    break
            else:
                cnt += 1
print(cnt)
