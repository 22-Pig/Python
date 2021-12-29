n = int(input())
for num in range(10**(n - 1), 10**n):
    lists = map(int, str(num))
    sum = 0
    for i in lists:
        sum += i**n
    if sum == num:
        print(num)