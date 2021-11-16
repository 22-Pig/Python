import math as m

a, b = map(eval, input().split())
c = m.factorial(a) / (m.factorial(a - b) * m.factorial(b))
print("%d" % c)
