n = int(input())
print(sum([1 / i if i % 2 == 1 else -1 / i for i in range(1, n + 1)]))
