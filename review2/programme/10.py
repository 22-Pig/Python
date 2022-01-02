n = int(input())
max = 0
for i in range(n):
    str1 = input().strip()
    if max <= len(str1):
        max = len(str1)
print('length=%d' % max)
