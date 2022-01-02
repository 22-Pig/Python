n = int(input())
num = 0
sum = 0
for i in range(n):
    dic = eval(input())
    # eval函数在这里就是说明dic接收的是一个字典
    # print(dic)
    for j in dic:
        temp = dic[j]
        for key in temp:
            # 计算边数和边总长度
            num += 1
            sum += temp[key]
print(n, num, sum)
