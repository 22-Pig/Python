numList = list(range(1, 31))  # 创建序号列表
i = 0  # 用来作报数循环
leaveList = []  # 存放离开的人序号
while (len(leaveList) < 10):  # 离开10人即结束
    for num in numList:
        if num not in leaveList:  # 除掉已离开的
            i += 1
            if i == 9:  # 报到9离开，进入离开的列表
                leaveList.append(num)
                i = 0
                if len(leaveList) == 10:  # 10个人时，跳出for语句循环
                    break  # 跳出整个循环
        else:
            next  # next跳出当前当次循环 进行num+1
print("离开的顺序为", leaveList)
