a = eval(input())
b = list(map(eval, input().split()))
b.sort(reverse=True)
for i in b[:3:]:
    print("%.1f" % i, end=" ")
