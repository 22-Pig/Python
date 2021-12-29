str = input()
newStr = ''
for i in str:
    num = ord(i)  # 得到ASCII码
    if (65 <= num <= 90):  # 如果是大写字母
        i = i.replace(i, chr(155 - num))
    newStr += i

print(newStr)