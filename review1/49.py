n = int(input())
if n < 1:
    print("Invalid.")
a = 0
b = 1
c = 1
count = 0
for i in range(n):
    print("{:>11d}".format(c), end="")
    c = a + b
    a = b
    b = c
    count += 1
    if count == 5 or i == n - 1:
        print("\n", end="")
        count = 0
