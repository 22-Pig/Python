# import math
from math import sqrt


def area(a, b, c):
    s = (a + b + c) / 2
    # return (math.sqrt(s * (s - a) * (s - b) * (s - c)))
    return (sqrt(s * (s - a) * (s - b) * (s - c)))
