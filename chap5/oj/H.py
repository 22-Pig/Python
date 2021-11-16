a, b = map(eval, input().split())
x = 0
for i in range(a, b + 1):
    n = i
    while n > 0:
        if n % 10 == 2:
            x += 1
        n //= 10
print(x)
