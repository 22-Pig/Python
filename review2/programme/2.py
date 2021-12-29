str1 = input()
a, b = input().split()
for i in range(len(str1) - 1, -1, -1):
    if str1[i] == b:
        print(i, b)
    if str1[i] == a:
        print(i, a)
