import random

digits=[chr(i) for i in range(48,58)]
ascii_letters=[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]

# 数字的个数随机产生
num_of_numeric = random.randint(1,7)
# 剩下的都是字母
num_of_letter = 8 - num_of_numeric
# 随机生成数字
numerics = [random.choice(digits) for i in range(num_of_numeric)]
# 随机生成字母
letters = [random.choice(ascii_letters) for i in range(num_of_letter)]
# 结合两者
all_chars = numerics + letters
# 重新排列
random.shuffle(all_chars)
# 生成最终字符串
result = ''.join([i for i in all_chars])
print(result)
