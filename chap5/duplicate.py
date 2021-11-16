# 列表去重,保持原有顺序
mailto = ['cc', 'bbbb', 'afa', 'sss', 'bbbb', 'cc', 'shafa']
# 将列表转换成集合再转换成列表（集合可以去重）
addr_to = list(set(mailto))
print(addr_to)
# print(mailto.index)
addr_to.sort(key=mailto.index)
# addr_to.sort()
print(addr_to)
