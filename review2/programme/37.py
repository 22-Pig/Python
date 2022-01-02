lst = [0, 34, 6, 0, 7, 0, 9]
n = 0
for i in lst:
    if i == 0:
        lst.remove(i)
        print(lst)
        n += 1
print(n)
