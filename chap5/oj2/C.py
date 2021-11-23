a = list(map(int, input().split()))
b = [
    28.1, 54.5, 46.6, 37.1, 38, 46.7, 70.7, 21.8, 31.4, 27.6, 39.3, 37.1, 56.7,
    70.3, 72.7, 40.7
]
sum = 0
for i in range(len(a)):
    sum += a[i] * b[i]
print("%.1f" % sum)
