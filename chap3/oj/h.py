n = eval(input())
g = n % 10
s = n // 10 % 10
b = n // 100
print('%d%d%d' % (g, s, b))
