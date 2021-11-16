str = input()
countchar = {}

for c in str:
    # countchar.get(c,0)函数返回键为c的值, 不在字典中返回0
    countchar[c] = countchar.get(c, 0) + 1
print(countchar)
