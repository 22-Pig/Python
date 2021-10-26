lower, upper = input().split()  # 一行输入两个数，是字符串类型
lower, upper = int(lower), int(upper)  # 字符串变成整数

for i in range(lower, upper, 2):
    print(i, "{:.1f}".format(5 * (i - 32) / 9))
