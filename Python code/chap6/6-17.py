pre={0:1,1:1}

def fib(n):
    if n in pre:	#可以用in检查字典中是否有n这个关键字
        return pre[n]
    else:
        newvalue=fib(n-1)+fib(n-2)
        pre[n]=newvalue #增加字典的条目
        return newvalue

print(fib(100))
