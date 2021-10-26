a, b, c = map(eval, input().split())
if a > b:
    temp = b
    b = a
    a = temp
if a > c:
    temp = c
    c = a
    a = temp
if b > c:
    temp = c
    c = b
    b = temp
print(a, b, c)
