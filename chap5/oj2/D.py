a = list(map(int, input().split()))
b = a[-1]
del a[-1]
if b in a:
    print("Yes")
else:
    print("No")
