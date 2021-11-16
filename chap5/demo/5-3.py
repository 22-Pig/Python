data = set()
while True:
    x = int(input())
    if x == -1:
        break
    data.add(x)
print('%d read.' % len(data))
