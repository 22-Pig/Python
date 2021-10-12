import math

a, b, c = map(int, input().split())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print('%.6f' % s)
# print("{:.6f}".format(s))
