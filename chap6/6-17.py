pre = {0: 1, 1: 1}


def fib(n):
    # 可以用in检查字典中是否有n这个关键字
    if n in pre:
        return pre[n]
    else:
        newvalue = fib(n - 1) + fib(n - 2)
        # 增加字典的条目
        pre[n] = newvalue
        return newvalue


print(fib(100))
