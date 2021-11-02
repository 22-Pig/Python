n = eval(input())
x = 0
a = 1
for i in range(n):
    x = x * 10 + a
    a = a + 1
    print(x)
