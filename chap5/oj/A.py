n = int(input())
list = []
for i in range(1, n):
    if n % i == 0:
        list.append(i)
if sum(list) == n:
    print('Yes')
else:
    print('No')
