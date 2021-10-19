# 掷10000次硬币，正面向上用1表示，反面向上用0表示。
import random
# 产生10000个随机数，值为0或1
rand = [random.randint(0, 1) for i in range(10000)]
print(sum(rand) / len(rand))
