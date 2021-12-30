n = input()
lst = []
for i in n:
    if 'a' < i < 'z' or 'A' < i < 'Z':
        lst.append(i.lower())
if lst == lst[::-1]:
    print('yes')
else:
    print('no')