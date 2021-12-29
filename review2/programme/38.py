letterNum = 0
blankNum = 0
digitNum = 0
otherNum = 0
count = 0
str = ""
while True:
    s = input()
    count += 1
    str += s
    if len(str) + count > 10:
        count -= 1
        break
blankNum += count
for i in str:
    # isalpha() 方法检测字符串是否只由字母组成
    if i.isalpha():
        letterNum += 1
    # isspace() 方法检测字符串是否只由空格组成
    elif i.isspace():
        blankNum += 1
    # isdigit() 方法检测字符串是否只由数字组成
    elif i.isdigit():
        digitNum += 1
    else:
        otherNum += 1
print("letter = {}, blank = {}, digit = {}, other = {}".format(
    letterNum, blankNum, digitNum, otherNum))