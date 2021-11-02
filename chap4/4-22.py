a = []
while True:
    x = int(input())
    if x == -1:
        break
    a.append(x)
maxidx = 0
for i in range(1, len(a)):
    if a[i] > a[maxidx]:
        maxidx = i
print(maxidx)
