data = []
while True:
    x = int(input())
    if x == -1:
        break
    if x not in data:
        data.append(x)
print('%d read.' % len(data))
