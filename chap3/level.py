# 第一层，输入层
s = input()
# 第二层
lst = [
    t for t in s if ord('0') <= ord(t) <= ord('9')
    or ord('a') <= ord(t) <= ord('f') or ord('A') <= ord(t) <= ord('F')
]

# 第三层
news = ''.join(lst)

# 第四层  输出层
print(news)
print(int(news, 16))
