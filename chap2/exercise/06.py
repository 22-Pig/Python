n = int(input())
a = 0
for x in range(1, n + 1):
    if x % 2 == 1:
        a = a + x / (2 * x - 1)
    else:
        a = a - x / (2 * x + 1)
print("{0:.3f}".format(a))
