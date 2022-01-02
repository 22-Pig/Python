s = input()
l1 = '0123456789abcdeABCDE'  # 大小写字母需要包含进去
l2 = ''
for i in s:
    if i in l1:
        print(i, end='')  # 防止换行
        l2 = l2 + i  # 组合十六进制数
print("\n{}".format(int(l2, 16)))  # 字符串转换成16进制整数
