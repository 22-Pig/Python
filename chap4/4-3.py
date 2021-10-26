# 读入投币金额
amount = int(input('请投币：'))
if amount >= 10:
    # 打印车票
    print('******************')
    print('*Python城际铁路专线*')
    print('*   票价：10元    *')
    print('******************')
    # 计算并打印找零
    print('找零：{}'.format(amount - 10))
