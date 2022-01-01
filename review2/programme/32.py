num = list(map(int, input().split()))
l = []
l.append(num[0] + num[4] + num[8])
l.append(num[2] + num[4] + num[6])
for i in range(0, 6, 3):
    l.append(num[i] + num[i + 1] + num[i + 2])
for j in range(0, 3, 1):
    l.append(num[j] + num[j + 3] + num[j + 6])
print(max(l))