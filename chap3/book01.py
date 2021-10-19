list = [int(x) for x in input().split()]

x = sum(list) / len(list)
for i in range(0, len(list)):
    if list[i] >= x:
        print(list[i], end=' ')
