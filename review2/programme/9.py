m = str(input())
n = eval(m[1:])
value = 0
if (m[0] == '$'):
    value = n * 7
    print('￥{:.2f}'.format(value))
elif (m[0] == '￥'):
    value = n / 7
    print('${:.2f}'.format(value))
else:
    print('输入格式错误')
