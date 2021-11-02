a = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37]
x = int(input())
found = -1
for i in range(len(a)):
    if a[i] == x:
        found = i
        break
print(found)
