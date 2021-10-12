x = int(input())
if x < 0:
    print("Invalid Value!")
if x <= 50 and x > 0:
    y = x * 0.53
    print("cost = %.2f" % y)
if x > 50:
    z = 50 * 0.53
    x = x - 50
    y = z + x * 0.58
    print("cost = %.2f" % y)
