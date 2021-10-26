a=[80, 58, 73, 90, 31, 92, 39, 24, 14, 79, 46, 61, 31, 61, 93, 62, 11, 52, 34, 17]
for right in range(len(a), 0, -1):
	for i in range(0, right-1):
		if a[i]>a[i+1]:
			a[i], a[i+1] = a[i+1], a[i]
	print(a)
