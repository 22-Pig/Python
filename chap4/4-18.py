num = int(input())
for i in range(num - 1, 1, -1):
    if num % i == 0:
        print('不是素数')
        break
else:
    print("是素数")
