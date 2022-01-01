s1 = input()
s2 = input()
count = 0
for i in s1:
    if i in s2:
        count += 1
print(count)