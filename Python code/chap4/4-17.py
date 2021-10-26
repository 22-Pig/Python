num=int(input())
a=num-1
while a>1:
   if num % a == 0:
        print("不是素数")
        break
   a=a-1
else:
   print("是素数")




