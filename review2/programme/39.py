def triangle():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i] + N[i - 1] for i in range(len(N))]


def print_triangle(x):
    a = 0
    for t in triangle():
        if len(t) == 1:
            print(t[0], "")
        else:
            for i in range(len(t)):
                print(t[i], end=' ')
            print()
        a += 1
        if a == x:
            break


num = int(input())
print_triangle(num)