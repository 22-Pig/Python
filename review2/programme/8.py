a = input()
b = input()
count = 0
for i in range(len(a)):
    if a.count(a[i]) == b.count(a[i]):
        count += 1
if count == len(a):
    print("yes")
else:
    print("no")
