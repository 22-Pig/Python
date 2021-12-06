while True:
    a = list(map(int, input().split()))
    del a[0]
    a.reverse()
    for i in a:
        print(i, end=' ')
    print('\n')
