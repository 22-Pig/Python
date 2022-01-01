list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
num = int(input())
for i in range(num):
    result = ''
    for j in range(i + 1):
        result += list1[j]
    print(result)