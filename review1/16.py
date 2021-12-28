a, n = input().split()
n = int(n)
a = float(a)
for i in range(n + 1):
    print("{0:.1f}**{1:d}={2:.2f}".format(a, i, pow(a, i)))
