name = input()     # 美化姓名
print("*" + name + "*")    # 输入姓名，美化后输出。

a, b = map(int, input().split())   # 计算两个整数的差
print("s=%d" % (a - b))        # 计算两个整数的差。

n = input()         # 输入学生姓名，输出问候信息
print("Hello," + n + "!")        # 输入学生姓名name，输出问候信息"Hello,name"。

m, n = map(int, input().split())     # A+B
print(m + n)          # 在学习程序设计课程的入门阶段，经常要编写一些简单的练习程序，例如：输出Hello,world或计算A+B

y = int(input())    # 输出日期
m = int(input())    # 本题目要求输入代表日期的3个整数Y（年）、M（月）和D（日），然后以“年-月-日”格式输出日期
d = int(input())
y, m, d = str(y), str(m), str(d)
print(y + "-" + m + "-" + d)

import math         # 求圆面积
x = eval(input())       # 输入圆的半径，求圆的面积（使用math库的pi常量）
area = math.pi * x**2
print('圆面积是{:.2f}'.format(area))

n = int(input())      # 重复多个星号
print(n * "*")        # 根据给定的整数n，在一行上打印n个*号

a, b = input().split()     # 交换两个整数
a, b = b, a          # 输入两个整数，交换位置后输出。
print('a=' + a, 'b=' + b)

m = str(input())   # 人民币与美元汇率兑换程序
n = eval(m[1:])    # 设计人民币与美元汇率兑换程序，按照1美元=7人民币的汇率 编写一个双向兑换程序
value = 0
if (m[0] == '$'):
    value = n * 7
    print('￥{:.2f}'.format(value))
elif (m[0] == '￥'):
    value = n / 7
    print('${:.2f}'.format(value))
else:
    print('输入格式错误')

lower, upper = map(int, input().split())   # 输出摄氏-华氏温度转换表
if (lower <= -20 or upper >= 50):    # 输入2个正整数lower和upper（-20<=lower<=upper<=50），表示摄氏范围。请输出一张取值范围为[lower，upper]、 且每次增加2摄氏度的摄氏-华氏温度转换表。温度转换的计算公式： F=C×1.8+32 其中：C表示摄氏温度，F表示华氏温度。
    print('Invalid.')
elif (lower > upper):
    print("Invalid.")
else:
    print("celsius    fahr")
    for C in range(lower, upper + 1, 2):
        F = C * 1.8 + 32
        print("{:d}{:>14.1f}".format(C, F))

n = int(input())  # 显示菱形图形
num = -1        # 显示菱形图形，每行的宽度是11。
for i in range(n):
    if i <= n // 2:
        num = num + 2
    else:
        num = num - 2
    numk = (11 - num) // 2
    print(' ' * numk, end='')
    print('*' * num, end='')
    print(' ' * numk)

from math import factorial  # 求误差小于输入值的e的近似值
error = float(input())  # 自然常数e可以用级数1+1/1!+1/2!+⋯+1/n!来近似计算。ei代表前i项求和。输入误差范围error,当ei+1-ei<error,则表示e的近似值满足误差范围
sum, i = 1, 1
while True:
    e1 = sum + 1 / factorial(i)
    i += 1
    e2 = e1 + 1 / factorial(i)
    i += 1
    sum = e2
    if e2 - e1 < error:
        print("%.6f" % e1)
        break

from math import sqrt  # 显示指定范围的素数并求和
m, n = map(int, input().split())  # 本题要求显示给定整数M和N区间内素数并对它们求和。
prime = []
def isPrime(p):
    if p == 1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True
for i in range(m, n + 1):
    if (isPrime(i)):
        prime.append(i)
count = 1
suma = 0
c = 0
for i in prime:
    if i > m:
        c += 1
        suma += i
        print(i, end=' ')
        if count % 5 == 0:
            print()
            count = 0
        count += 1
if count % 5 != 0:
    print()
print("amount=%d sum=%d" % (c, suma))

m = int(input())   # 分解素因子
for i in range(m):    # 假设n是一个正整数，它的值不超过1000000，请编写一个程序，将n分解为若干个素数的乘积
    n = int(input())
    x = 2
    # 从2开始到n的平方根，枚举每个自然数x
    while x <= n // x:
        # x是n的因子
        if n % x == 0:
            print(str(x) + "*", end="")
            n //= x
        else:
            x += 1
    print(n)

a = eval(input())    # 打印数字三角形图案
for i in range(1, a + 1):   # 本题目要求编写程序打印，输入一个正整数n（1<=n<=10)，输出由数字组成的三角形图案
    for j in range(1, i + 1):
        print(j, end='')
    print()

a, n = input().split()   # 生成输入数的乘方表
n = int(n)   # 输入一个非负数和正整数n，3<=n<=9，生成一张输入数的乘方表
a = float(a)
for i in range(n + 1):
    print("{0:.1f}**{1:d}={2:.2f}".format(a, i, pow(a, i)))

import math   # 求π的近似值
def fun(eps):           # 用公式求π的近似值：π 2 /6=1+1/2 2 +1/3 2 +1/4 2 +。。。当求和项小于误差时,结束求和。
    suma = 0
    count = 1
    c = 1
    while count > eps:
        count = 1 / math.pow(c, 2)
        suma += count
        c += 1
    return math.sqrt(suma * 6)
m = float(input())
print("{:.6f}".format(fun(m)))

num = int(input())   # 求分数序列前N项和
result = 0      # 本题要求编写程序，计算序列 2/1+3/2+5/3+8/5+... 的前N项之和。注意该序列从第2项起，每一项的分子是前一项分子与分母的和，分母是前一项的分子
deno = 2  # 首项分母
molec = 1  # 首项分子
for i in range(num):
    result += deno / molec
    mid = deno
    deno = deno + molec
    molec = mid
print("%.2f" % result)

x = eval(input())   # 计算分段函数1
if x == 0:   # 本题目要求计算下列分段函数f(x)的值
    res = 0
else:
    res = 1 / x
print('f({:.1f}) = {:.1f}'.format(x, res))

a, b = input().split()   # 输出华氏-摄氏温度转换表
a, b = eval(a), eval(b)   # 输入2个正整数lower和upper（lower≤upper≤100），请输出一张取值范围为[lower，upper]、且每次增加2华氏度的华氏-摄氏温度转换表。
if (a > b):
    print("Invalid.")
else:
    print("fahr celsius")
    i = a
    while i <= b:
        print("{:d}{:>6.1f}".format(i, 5 * (i - 32) / 9))
        i += 2

a = int(input())  # 求奇数分之一序列前N项和
sum = 0    # 本题要求编写程序，计算序列 1 + 1/3 + 1/5 + ... 的前N项之和
n = 1
for i in range(a):
    sum += 1 / n
    n += 2
print("sum = %.6f" % sum)

a = int(input())  # 阶梯电价
if (a < 0):   # 为了提倡居民节约用电，某省电力公司执行“阶梯电价”，安装一户一表的居民用户电价分为两个“阶梯”：月用电量50千瓦时（含50千瓦时）以内的，电价为0.53元/千瓦时；超过50千瓦时的，超出部分的用电量，电价上调0.05元/千瓦时。请编写程序计算电费
    print("Invalid Value!")
elif (a <= 50):
    cost = a * 0.53
    print("cost = {:.2f}".format(cost))
else:
    cost = 50 * 0.53 + (a - 50) * 0.58
    print("cost = {:.2f}".format(cost))

n = int(input())  # 求交错序列前N项和
sum = 0    # 本题要求编写程序，计算交错序列 1-2/3+3/5-4/7+5/9-6/11+... 的前N项之和
a = 1
b = 1
for i in range(n):
    if a % 2 == 0:
        sum -= a / b
    else:
        sum += a / b
    a += 1
    b += 2
print("%.3f" % sum)

a, b, c = map(int, input().split())   # 比较大小
if (a > b):     # 本题要求将输入的任意3个整数从小到大输出
    a, b = b, a
if (a > c):
    a, c = c, a
if (b > c):
    b, c = c, b
print("%d->%d->%d" % (a, b, c))

a, n = map(int, input().split())   # 特殊a串数列求和
sum = 0   # 给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和。
t = 0
for i in range(n):
    t = t * 10 + a
    sum = sum + t
print("s = {:d}".format(sum))

a, b = map(int, input().split(','))  # 产生每位数字相同的n位数
for i in range(b):      # 读入2个正整数A和B，1<=A<=9, 1<=B<=10,产生数字AA...A,一共B个A
    print(a, end='')

n = int(input())     # 计算 11+12+13+...+m
sum = 0         # 输入一个正整数m(20<=m<=100)，计算 11+12+13+...+m 的值
for i in range(11, n + 1):
    sum = sum + i
print("sum = {}".format(sum))

num, kind = input().split(',')     # 转换函数使用
print(int(num, base=int(kind)))    # 输入一个整数和进制，转换成十进制输出

a = int(input())   # 从键盘输入两个数，求它们的和并输出
b = int(input())   # 本题目要求读入2个整数A和B，然后输出它们的和
print(a + b)

a, b, c = map(int, input().split())   # 从键盘输入三个数到a,b,c中，按公式值输出
print(b * b - 4 * a * c)     # 在同一行依次输入三个值a,b,c，用空格分开，输出 b*b-4*a*c的值

a, b = map(eval, input().split())      # 求平方与倒数序列的部分和
sum = 0       # 本题要求对两个正整数m和n（m≤n）编写程序，计算序列和m 2 +1/m+(m+1) 2 +1/(m+1)+⋯+n 2 +1/n
for i in range(a, b + 1):
    sum = sum + i * i + 1 / i
print("sum = {:.6f}".format(sum))

import math
a, b, c = map(int, input().split())     # 输出三角形面积和周长
s = (a + b + c) / 2        # 本题要求编写程序，根据输入的三角形的三条边a、b、c，计算并输出面积和周长。
if s > max(a, b, c):  # 判断是否构成三角形
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = 2 * s
    print("area = %.2f" % area + "; " + "perimeter = %.2f" % perimeter)
else:
    print("These sides do not correspond to a valid triangle")

m = float(input())   # 分段计算居民水费
if (m <= 15):        # 为鼓励居民节约用水，自来水公司采取按用水量阶梯式计价的办法，居民应交水费y（元）与月用水量x（吨）相关：当x不超过15吨时，y=4x/3；超过后，y=2.5x−17.5。请编写程序实现水费的计算
    print("{:.2f}".format((4 * m) / 3))
else:
    print("{:.2f}".format(2.5 * m - 17.5))

m, n = map(int, input().split())         # 求整数段和
sum, count = 0, 0          # 给定两个整数A和B，输出从A到B的所有整数以及这些数的和
for i in range(m, n + 1):
    sum = sum + i
    count = count + 1
    print("{:>5d}".format(i), end="")
    if count % 5 == 0 or i == n:
        print()
print("Sum = %d" % sum)

n = int(input())    # 生成3的乘方表
for i in range(n + 1):      # 输入一个非负整数n，生成一张3的乘方表，输出3 0 ~3 n 的值。可调用幂函数计算3的乘方
    print("pow(3,%d) =" % i, pow(3, i))

n = int(input())    # 统计学生平均成绩与及格人数
if n == 0:           # 本题要求编写程序，计算学生们的平均成绩，并统计及格（成绩不低于60分）的人数。题目保证输入与输出均在整型范围内
    print("average = 0.0")
    print("count = 0")
    exit(0)
num = list(map(int, input().split()))
s, count = 0, 0
for i in num:
    s += i
    if i >= 60:
        count += 1
print("average = %.1f" % (s / n))
print("count = %d" % count)

letterNum = 0   # 统计字符
blankNum = 0    # 本题要求编写程序，输入10个字符，统计其中英文字母、空格或回车、数字字符和其他字符的个数
digitNum = 0
otherNum = 0
count = 0
str = ""
while True:
    s = input()
    count += 1
    str += s
    if len(str) + count > 10:
        count -= 1
        break
blankNum += count
for i in str:
    # isalpha() 方法检测字符串是否只由字母组成
    if i.isalpha():
        letterNum += 1
    # isspace() 方法检测字符串是否只由空格组成
    elif i.isspace():
        blankNum += 1
    # isdigit() 方法检测字符串是否只由数字组成
    elif i.isdigit():
        digitNum += 1
    else:
        otherNum += 1
print("letter = {}, blank = {}, digit = {}, other = {}".format(
    letterNum, blankNum, digitNum, otherNum))

print("[1] apple")    # 查询水果价格
print("[2] pear")       # 给定四种水果，分别是苹果（apple）、梨（pear）、桔子（orange）、葡萄（grape），单价分别对应为3.00元/公斤、2.50元/公斤、4.10元/公斤、10.20元/公斤
print("[3] orange")
print("[4] grape")
print("[0] exit")
price = [0.00, 3.00, 2.50, 4.10, 10.20]
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if i == 0:
        break
    elif 1 <= i <= 4:
        print('price = {:.2f}'.format(price[i]))
    else:
        print('price = 0.00')
    cnt += 1
    if cnt == 5:
        break

a = 1   # 求e的近似值
sum = 1           # 自然常数 e 可以用级数 1+1/1!+1/2!+⋯+1/n!+⋯ 来近似计算。本题要求对给定的非负整数 n，求该级数的前 n+1 项和。
n = int(input())
for i in range(1, n + 1):
    a *= i
    item = 1 / a
    sum += item
print("{:.8f}".format(sum))

sum = 0       # 统计素数并求和
count = 0             # 本题要求统计给定整数M和N区间内素数的个数并对它们求和。
m, n = map(int, input().split())
if m == 1:
    m += 1
for i in range(m, n + 1):
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        sum = sum + i
        count += 1
print("{:d} {:d}".format(count, sum))

num = int(input())       # 换硬币
count = 0              # 将一笔零钱换成5分、2分和1分的硬币，要求每种硬币至少有一枚，有几种不同的换法
for i in range(num // 5, 0, -1):
    for j in range(num // 2, 0, -1):
        for k in range(num, 0, -1):
            if 5 * i + 2 * j + k == num:
                print("fen5:{}, fen2:{}, fen1:{}, total:{}".format(
                    i, j, k, i + j + k))
                count += 1
print("count = {}".format(count))

def gcd(a, b):            # 最大公约数和最小公倍数
    if a > b:                 # 本题要求两个给定正整数的最大公约数和最小公倍数
        smaller = b
    else:
        smaller = a
    for i in range(smaller + 1):
        if a % (smaller - i) == 0 and b % (smaller - i) == 0:
            return smaller - i
def lcm(m, n):
    if m > n:
        greater = m
        smaller = n
    else:
        greater = n
        smaller = m
    i = 1
    while True:
        if greater * i % smaller == 0:
            return greater * i
        i += 1
x, y = map(int, input().split())
print('{:d} {:d}'.format(gcd(x, y), lcm(x, y)))

m = int(input())         # 猴子吃桃问题
ans = 1                 # 一只猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半加一个。到第N天早上想再吃时，见只剩下一个桃子了。问：第一天共摘了多少个桃子
for i in range(1, m):
    ans = (ans + 1) * 2
print(ans)

import math       # 验证“哥德巴赫猜想”
def issu(num):           # 数学领域著名的“哥德巴赫猜想”的大致意思是：任何一个大于2的偶数总能表示为两个素数之和。比如：24=5+19，其中5和19都是素数。本实验的任务是设计一个程序，验证20亿以内的偶数都可以分解成两个素数之和
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
m = int(input())
for i in range(2, m):
    if issu(i) and issu(m - i):
        print("{} = {} + {}".format(m, i, m - i))
        break

a, b, c = map(int, input().split())   # jmu-python-判断是否构成三角形
if a + b > c and a + c > b and b + c > a:        # 输入三角形的三边，判断是否能构成三角形。若能构成输出yes，否则输出no
    print("yes")
else:
    print("no")

import math            # 判断素数
def isPrime(p):      # 判断一个给定的正整数是否素数
    if p == 1:
        return False
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True
n = int(input())
while n > 0:
    num = int(input())
    if isPrime(num):
        print("Yes")
    else:
        print("No")
    n -= 1

n = int(input())         # 水仙花数
for num in range(10**(n - 1), 10**n):       # 水仙花数是指一个N位正整数（N≥3），它的每个位上的数字的N次幂之和等于它本身。 例如：153=1×1×1+5×5×5+3×3×3。本题要求编写程序,计算所有N位水仙花数
    lists = map(int, str(num))
    sum = 0
    for i in lists:
        sum += i**n
    if sum == num:
        print(num)

n = int(input())            # 输出前 n 个Fibonacci数
if n < 1:                  # 本题要求编写程序，输出菲波那契（Fibonacci）数列的前N项，每行输出5个，题目保证输出结果在长整型范围内。Fibonacci数列就是满足任一项数字是前两项的和（最开始两项均定义为1）的数列，例如：1，1，2，3，5，8，13，...。
    print("Invalid.")
a = 0
b = 1
c = 1
count = 0
for i in range(n):
    print("{:>11d}".format(c), end="")
    c = a + b
    a = b
    b = c
    count += 1
    if count == 5 or i == n - 1:
        print("\n", end="")
        count = 0

num = int(input())    # 求满足条件的斐波那契数
a = 1             # 斐波那契数，亦称之为斐波那契数列，指的是这样一个数列：1、1、2、3、5、8、13、21、……，这个数列从第3项开始，每一项都等于前两项之和。求大于输入数的最小斐波那契数
b = 1
c = a + b
while c < num:
    a, b = b, a + b
    c = a + b
print(c)

a=list(map(eval,input().split()))    # 大于身高的平均值
avg=sum(a)/len(a)      # 程序要输出那些超过输入的正整数的平均数的输入值，每个数后面有一个空格，输出的顺序和输入的相同。
for i in a:
    if i > avg:
        print(i,end=" ")

a=input()        # 输出字母在字符串中位置索引
b,c=map(str,input().split())   # 输入一个字符串，再输入两个字符，求这两个字符在字符串中的索引
lenth=len(a)
d=0
for i in a[::-1]:
    d += 1
    if i==b or i==c:
        print(lenth-d,i)

a=input()    # 求整数的位数及各位数字之和
b=len(a)      # 对于给定的正整数N，求它的位数及其各位数字之和。(提示：把整数转换成字符串，列表，用sum和len函数)
c=0
for i in a:
    c+=int(i)
print(b,c)

a=[chr(i) for i in range(65,91)]    # 字符替换
b=a[::-1]                           # 本题要求编写程序，将输入字符串中的大写英文字母按以下对应规则替换，其他字符不变。(提示：转换表用元组实现）
c=list(input())                           # 输入
f=0
for i in c:
    if i in a :
        d=a.index(i)                # 取出i在a中的下标
        e=b[d]                      # 获取在b中相同的下标字母
        c[f]=e                         # 将i改为e
    f += 1
print("".join(c))

aStr = input().strip()    # 删除字符
delete_chars = input().strip()    # 输入一个字符串 str，再输入要删除字符 c，大小写不区分，将字符串 str 中出现的所有字符 c 删除。提示：去掉两端的空格
print("result:",aStr.replace(delete_chars.upper(), "").replace(delete_chars.lower(), ""))

a=list(input())  # 输出10个不重复的英文字母
b=[]           # 随机输入一个字符串，把最左边的10个不重复的英文字母（不区分大小写）挑选出来。 如没有10个英文字母，显示信息“not found”
d=[]        # 存放大写字母的下标
for i in a:
    if 'A'<= i <='Z':
        c=i.lower()
        if c not in b:
            b+=c                    # 将原本是大写字母的小写字母加入b
            d.append(b.index(c))    # 将其下标加入D
    elif 'a'<=i <='z':
        if i not in b:
            b+=i
for i in d:                         # 遍历d，将其中存放的大写字母下标，变回大写字母
    b[i]=b[i].upper()

if len(b) < 10 :
    print('not found',end="")
else:
    print("".join(b[0:10]))

a=input()   # 逆序的三位数
if a[2]=="0" and a[1]=="0":      # 程序每次读入一个正3位数，然后输出按位逆序的数字。注意：当输入的数字含有结尾的0时，输出不应带有前导的0。比如输入700，输出应该是7
    print(a[0])
elif a[2]=="0":
    print(a[1::-1])
else:
    print(a[::-1])

a=input()        # 判断两个字符串是否为变位词
b=input()        # 如果一个字符串是 另一个字符串的重新排列组合，那么这两个字符串互为变位词。比如，”heart”与”earth”互为变位 词，”Mary”与”arMy”也互为变位词
count=0
for i in range(len(a)):
    if a.count(a[i]) == b.count(a[i]) :
        count+=1
if count == len(a):
    print("yes")
else:
    print("no")

a=list(input())   # 输入字符串，排序后输出最大字符及该字符在原字符串中的索引
l1=sorted(a)      # 输入字符串，排序后输出最大字符及该字符在原字符串中的索引。相同字符的索引取最大值。提示：用元组实现
b=0             # 下标
c=0
for i in a :
    if i == l1[-1]:
        c=b
    b+=1
print(l1[-1]," ",c)

a=int(input())    # 计算有n个字符串中最长的字符串长度
c=[]             # 编写程序，用于计算有n(1<n<10)个字符串中最长的字符串的长度。前导空格不要计算在内
for i in range(a):
    b=input().strip()
    c.append(len(b))
print("length=",max(c),sep="")

a=int(input())          # 位1的个数
b=str(bin(a))          # 输入一个非负整数，求它变成二进制后1的个数（提示：用bin函数）
c=0
for i in b:
    if i == "1":
        c+=1
print(c)

a=eval(input())          # 整数的二进制相加
b=eval(input())          # 输入两个整数，大小在[0,63]之间。求它们的二进制和，二进制用8位表示
c=a+b
a1=bin(a)
b1=bin(b)
c1=bin(c)
a2=int(a1[2:])
b2=int(b1[2:])
c2=int(c1[2:])
print("%08d"%(a2))
print("%08d"%(b2))
print("-"*8)
print("%08d"%(c2))

a,b=map(int,input().split())     # 汉明距离
c=a^b                   # 两个整数间的汉明距离指的是这两个数对应二进制位不同的位置的数目。输入两个整数x,y, 0<=x,y<=2^31 。输出x,y的汉明距离
c1=bin(c)
d=0
for i in c1:
    if i=="1":
        d+=1
print(d)

a=input()   # 判断回文字符串
b=[]            # 回文就是字符串中心对称，从左向右读和从右向左读的内容是一样的。 输入一个字符串，判断该字符串是否为回文，只考虑数字和字母字符，字母的大小写没有区别
for i in a:
    if "a"<=i<="z" or "A"<=i<="Z":
        b.append(i.lower())
if b==b[::-1]:
    print('yes')
else:
    print('no')

a=input()          # 输入一行字符串，并将它转换成10进制数输出
b=[]            # 输入一行字符串，去掉非16进制字符，并将它转换成10进制数输出
for i in a:
    if "0"<=i<="9" or "a"<=i<="f" or "A"<=i<="F":
        b.append(i)
print("".join(b))
print(int("".join(b),16))

a=input()           # 统计满足特定条件的字符数
b=input()           # 输入字符串A(没有重复字符），输入字符串B，求在字符串A中字符的个数，这些字符必须同时又在字符串B中。提示：用in运算符
c=0
for i in a:
    if i in b:
        c+=1
print(c)

n = int(input())        # 查验身份证
strs = []           # 一个合法的身份证号码由17位地区、日期编号和顺序编号加1位校验码组成。校验码的计算规则如下
for i in range(n):
    strs.append(input())
nums = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
data = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
t = True  # 判断是否有错误的身份证
for ch in strs:  # 遍历每个身份证
    s = True  # 判断每个位数是否为数字
    sum = 0  # 权和
    for i in range(17):  # 遍历每个位数
        if '0' <= ch[i] <= '9':  # 如果是数字则进行加权求和
            sum += int(ch[i]) * nums[i]
        else:  # 如果不是数字则令 s = False 并跳出循环
            s = False
            break
    if s:  # 判断各个位数是否为数字
        Z = sum % 11  # 如果是则进行取模运算
        if str(data[Z]) != ch[17]:
            t = False  # 如果取模运算结果和效验码不一样，则令 t = False 并输出错误身份证
            print(ch)
    else:
        t = False  # 如果前17位某一位不为数字，则直接令 t = False 并打印错误身份证
        print(ch)
if t:  # 判断是否有错误身份证，若没有则打印“All passed”
    print("All passed")

week={1:"Mon",2:"Tue",3:"Wed",4:"Thu",5:"Fri",6:"Sat",7:"Sun"}    # 输出星期名缩写
a=int(input())                        # 输入一个1到7的数字，输出对应的星期名的缩写
print(week[a])

n = int(input())   # 图的字典表示
num = 0          # 图的字典表示。输入多行字符串，每行表示一个顶点和该顶点相连的边及长度，输出顶点数，边数，边的总长度。比如上图0点表示：{'O':{'A':2,'B':5,'C':4}}。用eval函数处理输入，eval函数具体用法见第六章内置函数
sum = 0
for i in range(n):
    dic = eval(input())
    # eval函数在这里就是说明dic接收的是一个字典
    # print(dic)
    for j in dic:
        temp = dic[j]
        for key in temp:
            # 计算边数和边总长度
            num += 1
            sum += temp[key]
print(n,num,sum)

a=int(input())         # 四则运算
c=input()                    # 四则运算（用字典实现），比较c语言的switch语句
b=int(input())
szys={"+":a+b,"-":a-b,"*":a*b,"/":(a/b) if b!=0 else'divided by zero'}
if type(szys[c])==str:
    print(szys[c])
else:
    print("%.2f"%(szys[c]))

a=list(map(int,input().split(",")))          # 分析活动投票情况
b=[6,7,8,9,10]               # 利用集合分析活动投票情况。第一小队有五名队员，序号是1,2,3,4,5;第二小队也有五名队员，序号6,7,8,9,10。输入一个得票字符串，求第二小队没有得票的队员
for i in set(a):
    if 6<=i<=10:
        if i in b:
            b.remove(i)
for i in b[0:-1]:
    print(i,end=" ")
print(b[-1])

a=input()      # 统计字符出现次数
b=input()          # 本题要求编写程序，统计并输出某给定字符在给定字符串中出现的次数
c=0
for i in a:
   if i==b :
       c+=1
print(c)

a=input()    # 统计工龄
b=list(map(int,input().split()))              # 给定公司N名员工的工龄，要求按工龄增序输出每个工龄段有多少员工
c={}
b.sort()
for i in b:
    if i not in c:
        c[i]=1
    else:
        c[i]+=1
sorted(c)
for i in c.keys():
    print(i,end=":")
    print(c[i])

lst1 = eval(input())       # 列表去重
lst2 = list(set(lst1))          # 输入一个列表，去掉列表中重复的数字，按原来次序输出
lst2.sort(key = lst1.index)
print(' '.join(list(map(str, lst2))))

a,b=map(int,input().split())      # 能被3,5和7整除的数的个数
number=0                   # 求指定区间内能被3,5和7整除的数的个数
for i in range(a,b+1):
    if i % 105 ==0:
        number+=1
print(number)

n = int(input())           # 求矩阵鞍点的个数
values = [[int(s) for s in input().split()] for i in range(n)]              # 本题要求编写程序，求一个给定的n阶方阵的鞍点
row_max_list = [max(values[i]) for i in range(n)]  # 各行最大值
column_min_list = []  # 用来存储各列最小值
# 求各列最小值
for column in range(n):
    column_min = values[0][column]
    for row in range(1, n):
        if values[row][column] < column_min:
            column_min = values[row][column]
    column_min_list.append(column_min)  # column列最小值

count = 0
# 逐行、逐列地扫描矩阵
for row in range(n):
    for column in range(n):
        if values[row][column] == row_max_list[row] and values[row][column] == column_min_list[column]:
            count += 1  # 鞍点个数加1
print(count)

a=list(map(int,input().split(",")))          # 两数之和
b=int(input())                              # 给定一组整数，还有一个目标数，在给定这组整数中找到两个数字，使其和为目标数，如找到，解是唯一的。找不到则显示 "no answer"。输出的下标按从小到大排序。用一重循环加字典实现
t=True
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]+a[j]==b:
            print(i,j)
            t=False
            break
if t==True:
    print("no answer")

d1 = eval(input(""))     # 字典合并
d2 = eval(input(""))          # 输入用字符串表示两个字典，输出合并后的字典。字典的键用一个字母或数字表示。注意：1和‘1’是不同的关键字
d3 = {}
c = 0
for i in d1:
    if i in d2:
        d2[i] += d1[i]
    else:
        d2[i] = d1[i]
for k in d2:
    if type(k) == type("a"):
        d3[ord(k)] = 0
    if type(k) == type(1):
        d3[k] = 1
print('{', end='')
for j in sorted(d3):
    c += 1
    if d3[j] == 0:
        print('"{}":{}'.format(chr(j), d2[chr(j)]), end='')
    if d3[j] == 1:
        print('{}:{}'.format(j, d2[j]), end='')
    if c < len(d3):
        print(',', end='')
print('}')

a=int(input())        # 显示数字出现次数
b=input()            # 输入一个十进制正整数，转换成16进制数。再输入一个数(0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f）,统计这个数出现的次数
a16=hex(a)
numberb=0
for i in a16:
    if i ==b:
        numberb+=1
print(numberb)

n=int(input())     # 猴子选大王
ls=[]              # 一群猴子要选新猴王。新猴王的选择方法是：让N只候选猴子围成一圈，从某位置起顺序编号为1~N号。从第1号开始报数，每轮从1报到3，凡报到3的猴子即退出圈子，接着又从紧邻的下一只猴子开始同样的报数。如此不断循环，最后剩下的一只猴子就选为猴王。请问是原来第几号猴子当选猴王
for i in range(n):
    ls.append(i+1)
index=0
while len(ls)>1:
    index=(index+2)%len(ls)    # 注意是+2
    ls.pop(index)
print(ls[0])

x=int(input())    # 特定矩阵元素和
b=[]              # 给定一个n×n的方阵，本题要求计算该矩阵主、副对角线上的所有元素之和。主对角线为从矩阵的左上角至右下角的连线,副对角线为从矩阵的右上角至左下角的连线
sumb=0
for i in range(x):
    a=list(map(eval,input().split()))
    b.append(a)
    sumb+=(a[i]+a[x-1-i])
if x%2 !=0 :
    sumb-=b[x//2][x//2]
print("%.2f"%sumb)

x=list(map(eval,input().split()))       # 矩阵行、列、对角线和的最大值# 求一个3*3矩阵每行、每列及对角线和的最大值
# 将输入的9个数字转换成3*3的矩阵
a=[]
b=[]
c=[]
d=[]
for i in range(9):
    if 0<=i<=2:
        a.append(x[i])
    elif 3<=i<=5:
        b.append(x[i])
    elif 6<=i<=8:
        c.append(x[i])
d.append(a)
d.append(b)
d.append(c)
# 取出每行、每列及对角线和的最大值
hsum1=0
for i in range(3):
    hsum = 0
    for j in range(3):
        hsum+=d[i][j]
    if hsum>hsum1:
        hsum1=hsum
lsum1=0
for i in range(3):
    lsum=0
    for j in range(3):
        lsum+=d[j][i]
    if lsum>lsum1:
        lsum1=lsum
zdsum1=0
for i in range(3):
    zdsum1+=d[i][i]
fdsum1=0
for i in range(3):
    fdsum1+=d[i][2-i]
# 判断：
maxsum=[]
maxsum.append(hsum1)
maxsum.append(lsum1)
maxsum.append(zdsum1)
maxsum.append(fdsum1)
print(max(maxsum))

num = int(input())     # 判断三角矩阵
s=[]              # 本题要求编写程序，判断一个给定的方阵是否是三角矩阵。三角矩阵包含上三角矩阵和下三角矩阵两种
for i in range(num):
    s1,s2=0,0
    count = int(input())
    for i in range(count):
        n=input()
        s.append([int(i) for i in n.split()])
    for index_h in range(count):
        for index_l in range(count):
            if index_l > index_h:
                s1+=s[index_h][index_l]
            elif index_l < index_h:
                s2+=s[index_h][index_l]
    if s1==0 and s2!=0:
        print("lower triangular matrix")
    elif s1!=0 and s2==0:
        print("upper triangular matrix")
    else:
        print("no")
    s=[]

a=int(input())        # 打印九九口诀表
for i in range(1,a+1):           # 本题要求对任意给定的一位正整数N，输出从1*1到N*N的部分口诀表
    for j in range(1,i+1):
        print("{}*{}={:<4d}".format(j,i,j*i),end="")
    print()

m, n = map(int, input().split())     # 求矩阵的局部极大值
a = []               # 给定M行N列的整数矩阵A，如果A的非边界元素A[i][j]大于相邻的上下左右4个元素，那么就称元素A[i][j]是矩阵的局部极大值。本题要求给定矩阵的全部局部极大值及其所在的位置
for i in range(m):
    a.append(list(map(int, input().split())))
t = False
for i in range(1, m - 1):# 不循环边缘元素
    for j in range(1, n - 1):
        data = [] # 存储四周的四个值
        data.append(int(a[i - 1][j]))
        data.append(int(a[i + 1][j]))
        data.append(int(a[i][j - 1]))
        data.append(int(a[i][j + 1]))
        if a[i][j] > max(data):
            print(a[i][j], i + 1, j + 1)
            t = True
if t == False:
    print("None",  m, n)

a,b=map(int,input().split())         # 矩阵转置
c=[]                    # 从键盘输入一个m(2<=m<=6)*n(2<=n<=6)阶的矩阵，编程输出它的转置矩阵
ls=[]
for i in range(a):
    d=input().split()
    c.append(d)
for i in range(b):
    d=[]
    for j in range(a):
        d.append(c[j][i])
    print(" ".join(d))

a=int(input())             # 显示直角数字图形
for i in range(1,a+1):              # 本题目要求输入行数，输出指定行数的图形
    for j in range(i):
        print(chr(ord("A")+j),end="")
    print()

n=eval(input())       # 显示菱形图形
a=int(n/2)               # 显示菱形图形，每行的宽度是11
b=5
for i in range(a):
    print(" "*(b-i-1),"*"*(i*2+1)," "*(b-i-1))
if a==5:
    print("*"*11)
    a=a-1
for i in range(a,-1,-1):
    print(" "*(b-i-1),"*"*(i*2+1),' '*(b-i-1))

def triangle():            # 显示Pascal三角形
    N = [1]            # 输入行数n,显示n行Pascal三角形。数字间有一个空格。每行最后一个数字后有一个空格
    while True:
        yield N
        N.append(0)
        N = [N[i]+N[i-1] for i in range(len(N))]
def print_triangle(x):
    a = 0
    for t in triangle():
        if len(t)==1:
            print(t[0],"")
        else:
            for i in range(len(t)):
                print(t[i],end=' ')
            print()
        a += 1
        if a ==x:
            break
num=int(input())
print_triangle(num)

a=eval(input())             # 输入列表，求列表元素和(eval输入应用）
print(sum(a))          # 在一行中输入列表，输出列表元素的和

a=int(input())     # 一帮一
f=[]          # 本题就请你编写程序帮助老师自动完成这个分配工作，即在得到全班学生的排名后，在当前尚未分组的学生中，将名次最靠前的学生与名次最靠后的异性学生分为一组
m=[]
d=[]
for i in range(a):
    temp = input().split()
    d.append(temp[1])
    if temp[0] == "0":
        f.append(temp[1])
    else:
        m.append(temp[1])
d=d[:a//2]
f=f[::-1]
m=m[::-1]
f1=0
m1=0
for i in range(len(d)):
    if d[i] in m:
        print(d[i],f[f1])
        f1+=1
    else:
        print(d[i],m[m1])
        m1+=1

import math           # 验证“哥德巴赫猜想”
def isP(a):                   # 数学领域著名的“哥德巴赫猜想”的大致意思是：任何一个大于2的偶数总能表示为两个素数之和。比如：24=5+19，其中5和19都是素数。本实验的任务是设计一个程序，验证20亿以内的偶数都可以分解成两个素数之和
    if a <= 1:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i == 0:
            return False
    return True
a=int(input())
for i in range(2,a//2+1):
    b=a-i
    if isP(b) and isP(i):
        print("{} = {} + {}".format(a,i,b))
        break

a = eval(input())          # 列表或元组的数字元素求和
def fn(base):                 # 求列表中数字和,列表中嵌套层次不限2层
    if type(base) == int:
        return base
    else:
        return sum(fn(i) for i in base if type(i) != str)
print(fn(a))

a = input()       # 列表数字元素加权和
n = 0            # 输入一个嵌套列表，嵌套层次不限，根据层次，求列表元素的加权和。第一层每个元素 的值为：元素值*1，第二层每个元素的值为：元素值*2，第三层每个元素的值为：元素值*3， ...,以此类推
ans = 0
backup = a
a = a.replace('[', '')
a = a.replace(']', '')
nums = a.split(',')
b = backup
j = 0
for i in range(len(b)):
    if b[i] == '[':
        n += 1
    elif b[i] == ']':
        n -= 1
    elif b[i] == ',':
        continue
    elif b[i+1] == ',' or b[i+1] == ']':
        ans += int(nums[j]) * n
        j += 1
print(ans)

a = eval(input())          # 列表元素个数的加权和
def fn(base, power):           # 输入一个嵌套列表，嵌套层次不限，根据层次，求列表元素的加权个数和。第一层每个元素算一个元素，第二层每个元素算2个元素，第三层每个元素算3个元素，第四层每个元素算4个元素
    if type(base) == int:
        return power
    else:
        return sum(fn(i, power+1) for i in base)
print(fn(a, 0))

a = eval(input())          # 求指定层的元素个数
b = int(input())              # 输入一个嵌套列表，再输入层数，求该层的数字元素个数
out = {}
def fn(base, ceng):
    for i in base:
        if type(i) == int:
            out[ceng] = out.get(ceng, 0) + 1
        else:
            fn(i, ceng + 1)
fn(a, 1)
print(out.get(b, 0))


# 6-1 使用函数求特殊a串数列和
# 给定两个均不超过9的正整数a和n，要求编写函数fn(a,n) 求a+aa+aaa++⋯+aa⋯aa(n个a）之和，fn须返回的是数列和
def fn(a, n):
    if n == 1:
        return a
    else:
        return eval(str(a) * n) + fn(a, n - 1)


#  使用函数求素数和
# 
# prime(p), 其中函数prime当用户传入参数p为素数时返回True，否则返回False. PrimeSum(m,n),函数PrimeSum返回区间[m, n]内所有素数的和。题目保证用户传入的参数1<=m<n。
from math import sqrt


def isPrime(p):
    if p == 1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


def PrimeSum(m, n):
    sum = 0
    for i in range(m, n + 1):
        if (isPrime(i)):
            sum += i
    return sum

# 6-3 使用函数统计指定数字的个数
# 本题要求实现一个统计整数中指定数字的个数的简单函数。
# 
# CountDigit(number,digit )
# 
# 其中number是整数，digit为[1, 9]区间内的整数。函数CountDigit应返回number中digit出现的次数。
def CountDigit(number, digit):
    number, digit = str(number), str(digit)
    return number.count(digit)


# 6-4 使用函数输出指定范围内Fibonacci数的个数
# 本题要求实现一个计算Fibonacci数的简单函数，并利用其实现另一个函数,输出两正整数m和n（0<m<n≤100000）之间的所有Fibonacci数的数目。 所谓Fibonacci数列就是满足任一项数字是前两项的和（最开始两项均定义为1）的数列,fib(0)=fib(1)=1。其中函数fib(n)须返回第n项Fibonacci数；函数PrintFN(m,n)用列表返回[m, n]中的所有Fibonacci数。
pre = {0: 1, 1: 1}


def fib(n):
    if n in pre:
        return pre[n]
    else:
        newValue = fib(n - 1) + fib(n - 2)
        pre[n] = newValue
        return newValue


def PrintFN(m, n):
    lst = []
    i = 0
    while fib(i) <= n:
        if fib(i) >= m:
            lst.append(fib(i))
        i += 1
    return lst


# 6-5 使用函数求余弦函数的近似值
# 本题要求实现一个函数，用下列公式求cos(x)近似值，精确到最后一项的绝对值小于eps（绝对值小于eps的项不要加）

import math


def funcos(eps, x):
    s = 0
    i = 0
    while True:
        temp = ((-1)**(i / 2)) * (x**i) / math.factorial(i)
        if abs(temp) >= eps:
            s += temp
        elif abs(temp) < eps:
            break
        i += 2
    return s


# 6-6 缩写词
# 缩写词是由一个短语中每个单词的第一个字母组成，均为大写。例如，CPU是短语“central processing unit”的缩写。

def acronym(phrase):
    return "".join([i[0].upper() for i in phrase.split()])


# 6-7 求嵌套列表的平均值
# Avg是一个求平均值的函数。它的参数是嵌套列表，求每个元素的平均值。每个元素是列表，至少有1个值。
def Avg(lst):
    blst = []
    for i in range(len(lst)):
        sum = 0
        avg = 0

        for j in range(len(lst[i])):
            sum = sum + lst[i][j]
        avg = sum / len(lst[i])
        blst.append(avg)
    return blst


# 6-8 求多项式的值 
# 一元多项式可以用列表表示

def polyvalue(lst, y):
    res = 0
    for i in range(len(lst)):
        res = res + lst[i] * (y**i)
    return res