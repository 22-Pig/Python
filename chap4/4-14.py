a, b = map(int, input("请输入两个整数：").split())
r = a % b
while r > 0:
    a, b = b, r
    r = a % b
print("最大公约数是{}".format(b))
