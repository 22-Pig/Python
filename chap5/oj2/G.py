while True:
    try:
        a = eval(input())
        b = str(bin(a))
        if a >= 0:
            print(b[2:])
        elif a < 0:
            print('-', b[3:], sep='')
    except:
        break
