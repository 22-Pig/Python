m, n = map(int, input().split())
sum, count = 0, 0
for i in range(m, n + 1):
    sum = sum + i
    count = count + 1
    print("{:>5d}".format(i), end="")
    if count % 5 == 0 or i == n:
        print()
print("Sum = %d" % sum)
