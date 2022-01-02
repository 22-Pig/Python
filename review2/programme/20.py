a = int(input())
c = input()
b = int(input())
szys = {
    "+": a + b,
    "-": a - b,
    "*": a * b,
    "/": (a / b) if b != 0 else 'divided by zero'
}
if type(szys[c]) == str:
    print(szys[c])
else:
    print("%.2f" % (szys[c]))
