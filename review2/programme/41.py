students = []
# 存储女孩的名字 根据名次排序
girl = []
# 存储男孩的名字 根据名次排序
boy = []
n = int(input())
for i in range(n):
    student = input().split()
    students.append(student[1])
    if student[0] == '0':
        boy.append(student[1])
    else:
        girl.append(student[1])

# 遍历前4名
for i in range(n // 2):
    # 如果是男孩
    if students[i] in boy:
        # index() 方法返回指定值首次出现的位置
        index = boy.index(students[i])
        print("{} {}".format(students[i], girl[-1 - index]))
    else:
        index = girl.index(students[i])
        print("{} {}".format(students[i], boy[-1 - index]))
