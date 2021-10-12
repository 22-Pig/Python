list = input().split()
olist = []
s = 0
for i in list:
    if int(i) > 0:
        # .append() 当前序列追加
        olist.append(int(i))
for i in olist:
    if i % 2 != 0:
        s += i
print(s)
