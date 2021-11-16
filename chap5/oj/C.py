n = int(input())
a, s = 0, 0
for i in range(1, n + 1):
    a = a + i  # 计算an
    s = s + a  # 计算累加和
print(s)
