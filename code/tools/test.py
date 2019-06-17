
from functools import reduce


def f(*arrs):
    return reduce(lambda t, s: t + s, arrs, [])

a = [0], [1], [3]
c = f(*a)
print(c)
