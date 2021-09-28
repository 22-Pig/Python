print(
    sum([1 / i if i % 4 == 1 else -1 / i for i in range(1, 50) if i % 2 == 1]))
