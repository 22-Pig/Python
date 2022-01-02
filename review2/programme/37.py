<<<<<<< HEAD
lst = [0, 34, 6, 0, 7, 0, 9]
n = 0
for i in lst:
    if i == 0:
        lst.remove(i)
        print(lst)
        n += 1
print(n)
=======
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
num = int(input())
for i in range(num):
    result = ''
    for j in range(i + 1):
        result += list1[j]
    print(result)
>>>>>>> 4d0cc0186e62cea2072127df4b846abba88a58b9
