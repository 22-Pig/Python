num = int(input())
s = []
sum1 = 0
sum2 = 0
for i in range(num):
    str1 = input().split(' ')
    s.append(str1)
for i in range(num):
    for k in range(num):
        if i == k:
            sum1 += float(s[i][k])
    for j in range(num):
        if i + j == num - 1:
            sum2 += float(s[i][j])
if num % 2 != 0:
    sum2 = sum2 - float(s[num // 2][num // 2])
print("{:.2f}".format(sum1 + sum2))
