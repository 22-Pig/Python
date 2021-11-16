# 用字典计数
# 输入一行字符，求字符”a”,”b”和”c”出现的次数
# 字典初始化
diccount = {char: 0 for char in "abc"}
s = input()
lst = [char for char in s if ord("a") <= ord(char) <= ord("c")]
print(lst)
for char in lst:
    diccount[char] += 1
print(diccount)
