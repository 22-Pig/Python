numerator = 2
denominator = 1
sum = 0
while True:
    try:
        n = int(input())
    except ValueError:
        print("输入错误，请输入整数")
    else:
        for i in range(n):
            sum += numerator / denominator
            numerator, denominator = numerator + denominator, numerator
        print('%.6f' % sum)
        break
