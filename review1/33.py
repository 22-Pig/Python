import math

a, b, c = map(int, input().split())
s = (a + b + c) / 2
if s > max(a, b, c):  # 判断是否构成三角形
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = 2 * s
    print("area = %.2f" % area + "; " + "perimeter = %.2f" % perimeter)
else:
    print("These sides do not correspond to a valid triangle")