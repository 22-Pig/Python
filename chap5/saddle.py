# 找鞍点（一个矩阵元素的“鞍点”是指该位置上的元素值在该行上最大、在该列上最小，设只有一个鞍点）
n = int(input())
a = []
for i in range(0, n):
    b = input().split()
    a.insert(i, b)
c = []
d = []
for i in range(0, n):
    maxa = max(int(a[i][j]) for j in range(n))
    mina = min(int(a[k][i]) for k in range(0, n))
    c += [(i, j) for j in range(n) if int(a[i][j]) == maxa]
    d += [(k, i) for k in range(n) if int(a[k][i]) == mina]
c = list(set(c) & set(d))
if (c != []):
    print(c[0])
else:
    print("NONE")
