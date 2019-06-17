import random
from functools import reduce


def random_values(count):
    return [random.random() for _ in range(count)]

def concat_arrays(arrs):
    return reduce(lambda t, s: t + s, arrs, [])


def cycle_right_array(arr, i, ):
    return arr[i:] + arr[:i]



def split_for_directions(start_val, count):
    remainder = count % 4
    whole = [[i + start_val]*(count//4) for i in range(4)]
    if remainder > 0:
        rest = [True]*remainder + [False]*(4 - remainder)
        random.shuffle(rest)
        for direction in range(4):
            if rest[direction]:
                whole[direction].append(direction + start_val)
    return concat_arrays(whole)

def calculate_view_size(north_view):
    width = north_view[1] + 1 + north_view[3]
    height = north_view[0] + 1 + north_view[2]
    return width, height



