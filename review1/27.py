lst = list(map(int, input().split(',')))
num = int(input())
d = {}
for i in lst:
    d[i] = num - i  # 把值对应到字典里面
for key, value in d.items():
    if key in lst and value in lst:  # key+value=num，如果都在l里说明就是两数之和
        print(lst.index(key), lst.index(value))  # 输出下标
        break
else:
    print("no answer")
