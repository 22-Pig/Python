import random

l = [random.randint(0, 1) for i in range(10000)]
print(sum(l) / len(l))
