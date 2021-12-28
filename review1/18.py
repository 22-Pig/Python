num = int(input())
result = 0
deno = 2  # 首项分母
molec = 1  # 首项分子
for i in range(num):
    result += deno / molec
    mid = deno
    deno = deno + molec
    molec = mid
print("%.2f" % result)
