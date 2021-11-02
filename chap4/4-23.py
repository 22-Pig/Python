a = [
    11, 14, 17, 24, 31, 31, 34, 39, 46, 52, 58, 61, 61, 62, 73, 79, 80, 90, 92,
    93
]
x = int(input())
found = -1
left = 0
right = len(a) - 1
while left <= right:
    mid = (left + right) // 2
    if a[mid] > x:
        right = mid - 1
    elif a[mid] < x:
        left = mid + 1
    else:  # a[mid]==x
        found = mid
        break
print(found)
