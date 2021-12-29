n = int(input())
strs = []
for i in range(n):
    strs.append(input())

nums = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
data = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}

t = True  # 判断是否有错误的身份证

for ch in strs:  # 遍历每个身份证
    s = True  # 判断每个位数是否为数字
    sum = 0  # 权和
    for i in range(17):  # 遍历每个位数
        if '0' <= ch[i] <= '9':  # 如果是数字则进行加权求和
            sum += int(ch[i]) * nums[i]
        else:  # 如果不是数字则令 s = False 并跳出循环
            s = False
            break
    if s:  # 判断各个位数是否为数字
        Z = sum % 11  # 如果是则进行取模运算
        if str(data[Z]) != ch[17]:
            t = False  # 如果取模运算结果和效验码不一样，则令 t = False 并输出错误身份证
            print(ch)
    else:
        t = False  # 如果前17位某一位不为数字，则直接令 t = False 并打印错误身份证
        print(ch)

if t:  # 判断是否有错误身份证，若没有则打印“All passed”
    print("All passed")
