a = [2,3,5,7,11,13,17,23,29,31,37]
x = int(input())
found = False
for k in a:
	if k == x:
		found = True
		break
print(found)
