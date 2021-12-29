num = int(input())
count = 0
for i in range(num // 5, 0, -1):
    for j in range(num // 2, 0, -1):
        for k in range(num, 0, -1):
            if 5 * i + 2 * j + k == num:
                print("fen5:{}, fen2:{}, fen1:{}, total:{}".format(
                    i, j, k, i + j + k))
                count += 1
print("count = {}".format(count))
