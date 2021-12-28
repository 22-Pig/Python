n = int(input())
if n == 0:
    print("average = 0.0")
    print("count = 0")
    exit(0)
num = list(map(int, input().split()))
s, count = 0, 0
for i in num:
    s += i
    if i >= 60:
        count += 1
print("average = %.1f" % (s / n))
print("count = %d" % count)
