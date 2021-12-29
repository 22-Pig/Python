lower, upper = map(int, input().split())
if (lower <= -20 or upper >= 50):
    print('Invalid.')
elif (lower > upper):
    print("Invalid.")
else:
    print("celsius    fahr")
    for C in range(lower, upper + 1, 2):
        F = C * 1.8 + 32
        print("{:d}{:>14.1f}".format(C, F))
