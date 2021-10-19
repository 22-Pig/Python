#输入一行字符串，过滤掉所有非16进制字符产生新字符串，
#输出新字符串，并将它转换成10进制数输出。

s=input()
lst=[t for t in s if ord('0')<=ord(t)<=ord('9')
     or ord('a')<=ord(t)<=ord('f')
     or ord('A')<=ord(t)<=ord('F')]
news=''.join(lst)
print(news)
print(int(news,16))
