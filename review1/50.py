num = int(input())
a = 1
b = 1
c = a + b
while c < num:
    a, b = b, a + b
    c = a + b
print(c)