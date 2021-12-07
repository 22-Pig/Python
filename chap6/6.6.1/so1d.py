students = [('江幸', 89, 15), ('方鹏', 80, 14), ('陈可', 85, 14)]
# 按年龄从小到大排序
print(sorted(students, key=lambda s: s[2]))
# 按成绩从大到小降序
print(sorted(students, key=lambda s: s[1], reverse=True))
[('江幸', 89, 15), ('陈可', 85, 14), (' 方鹏', 80, 14)]
