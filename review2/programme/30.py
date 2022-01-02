n = int(input())
ls = []
for i in range(n):
    ls.append(i + 1)
index = 0
while len(ls) > 1:
    index = (index + 2) % len(ls)  # 注意是+2
    ls.pop(index)
print(ls[0])