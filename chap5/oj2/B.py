a = list(map(int, input().split()))
del a[0]
# 列表反向
a.reverse()
for i in a:
    print(i, end=' ')
