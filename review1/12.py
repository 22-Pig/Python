from math import factorial

error = float(input())

sum, i = 1, 1
while True:
    e1 = sum + 1 / factorial(i)
    i += 1
    e2 = e1 + 1 / factorial(i)
    i += 1
    sum = e2
    if e2 - e1 < error:
        print("%.6f" % e1)
        break
