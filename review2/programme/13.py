x, y = map(int, input().split())


def hammingDistance(x, y):
    return bin(x ^ y).count("1")


print(hammingDistance(x, y))
