set0 = set(map(int, input().split(",")))
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
set3 = set2 - set0
print(*sorted(list(set3)))
