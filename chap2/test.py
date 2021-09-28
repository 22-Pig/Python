""" s = input()
if s[0] == '$':
    c = eval(s[1:])
    print("￥{:.2f}".format(7 * c))
elif s[0] == '￥':
    f = eval(s[1:])
    print("${:.2f}".format(f / 7))
else:
    print("输入格式错误") """

# str.format()
x = 3.14159
y = 2 * x * 3
print('{0:.2f}' '{1:.2f}'.format(x, y))
