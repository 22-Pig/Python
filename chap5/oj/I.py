n = eval(input())
a = n
b = 2
while a > 1:
    while (a % b == 0):
        a = a // b
        print(b, end="")
        if (a > 1):
            print('*', end="")
    b += 1
