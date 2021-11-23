a = eval(input())
b = list(map(int, input().split()))
c = eval(input())
d = 0
for i in b:
    if c == i:
        d += 1
print(d)
