list = [int(x) for x in input().split()]

x = sum(list) / len(list)
for i in range(0, len(list)):
    if list[i] >= x:
        print(list[i], end=' ')

# a = list(map(int, input().split()))

# b = sum(a) / len(a)

# for i in a:
#     if i >= b:
#         print(i, end=' ')
