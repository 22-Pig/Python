#掷10000次硬币，正面向上用1表示，反面向上用0表示。
import random    
l=[random.randint(0,1) for i in range(10000)]  #产生10000个随机数，值为0或1
print(sum(l)/len(l))
