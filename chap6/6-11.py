# 计算参数个数
def countnum(a, **d):
    print(d)
    print(len(d) + 1)


countnum(3, x1=9, x2=1, x3=6, x4=89)
