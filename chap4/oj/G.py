a, b = map(eval, input().split())
if a == 0 or b == 0:
    print('0.0')
else:
    r = (a * b) / (a + b)
    r = '%.1f' % r
    print(r)
