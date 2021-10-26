x, y = map(int, input().split())
if x > y:
    max = x
if y >= x:
    max = y
print(max)
