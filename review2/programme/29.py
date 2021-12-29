num_10 = int(input())
s_num = input()
t_16 = list(hex(num_10))
count = 0
for i in t_16:
    if s_num == i:
        count += 1
print(count)