import random
number = random.randint(0,100)
count = 0
while True:
    a = int(input('输入你猜的数:'))
    count += 1
    if a == number:
        break
    elif a>number:
        print('你猜的大了')
    else:
        print('你猜的小了')
print('猜中了！你用了{}次！'.format(count))



