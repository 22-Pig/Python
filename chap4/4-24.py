a = [
    80, 58, 73, 90, 31, 92, 39, 24, 14, 79, 46, 61, 31, 61, 93, 62, 11, 52, 34,
    17
]
for right in range(len(a), 0, -1):
    maxidx = 0
    for i in range(1, right):
        if a[i] > a[maxidx]:
            maxidx = i
    print('{} max {} at {}'.format(a, a[maxidx], maxidx))
    a[maxidx], a[right - 1] = a[right - 1], a[maxidx]
# print(a)
