def fib(n): #假定n是正整数，返回下标为n个斐波那契数
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))
