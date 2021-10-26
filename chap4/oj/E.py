from math import sqrt  # 导入防止sqrt报错

a, b, c = map(eval, input().split())
if (b**2) - (4 * a * c) > 0:  # 双根情况
    x1 = (-b + sqrt((b**2) - (4 * a * c))) / (2 * a)
    x2 = (-b - sqrt((b**2) - (4 * a * c))) / (2 * a)
    if x2 > x1:
        x1, x2 = x2, x1  # 确保x1 > x2
        print('x1=%.1f' % x1)
        print('x2=%.1f' % x2)
    else:
        print('x1=%.1f' % x1)
        print('x2=%.1f' % x2)
elif (b**2) - (4 * a * c) == 0:  # 单根情况
    x1 = (-b + sqrt((b**2) - (4 * a * c))) / (2 * a)
    print('x1=%.1f' % x1)
    print('x2=%.1f' % x1)
else:  # 无根情况
    print('no real solution')
