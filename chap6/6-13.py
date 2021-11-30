l = [2, 3, 5, 8, 3, 6, 8]
seen = set()
l1 = [i for i in l if i not in seen and not seen.add(i)]
# print(seen)
print(l1)
