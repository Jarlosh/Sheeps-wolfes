import random


# region stuff
import time
import timeit


def cycle_right_array(arr, i, ):
    return arr[i:] + arr[:i]


def gen_views(north_view):
    return [cycle_right_array(north_view, -i) for i in range(4)]


def cr_array(width, height):
    return [[0] * width for _ in range(height)]


# endregion


mp_borders = [0, 99, 99, 0]

# region merging arrays
def unite_two_arrays(parts, is_vertical, arg):
    if is_vertical:
        return parts[0] + parts[1]
    else:
        return [parts[0][y] + parts[1][y] for y in range(len(parts[0]))]


def unite_four_arrays(parts):
    columns = [
        unite_two_arrays((parts[0], parts[2]), True),  # 0 1  parts order
        unite_two_arrays((parts[1], parts[3]), True)   # 2 3
    ]
    return unite_two_arrays(columns, False)
# endregion

class Map:
    def __init__(self, width, height, mp):
        # self.mp = cr_array(width, height)
        self.mp = mp
        self.width = width
        self.height = height

    def _unsafe_sub(self, x, y, dx, dy):
        # we mean what x, y, dx, dy >= 0
        # and x + dx < width, y + dy < height
        return [row[x:x + dx] for row in self.mp[y:y + dy]]

    def go(self, x, y, view):
        top = y - view[0]
        right = x + view[1]
        bottom = y + view[2]
        left = x - view[3]
        width = view[1] + 1 + view[3]
        height = view[2] + 1 + view[4]
        # [8 1 2]  % outcomes numbers %
        # [7 0 3]   outcomes on borders means
        # [6 5 4]       tor property usage
        parts = []


        is_vert = False
        if left >= 0:
            if right < self.width:  # 0 | 1 | 5
                if top >= 0:
                    if bottom < self.height:    # 0
                        parts = [(left, top, width, height)]
                    else:                       # 5
                        parts = [
                            (left, top, width, self.height - top),
                            (left, 0, width, bottom - self.height)
                        ]
                        is_vert = True
                else:                           # 1
                    parts = [
                        (left, self.height - height - top, width, 0),
                        (left, 0, width, height + top)
                    ]
                    is_vert = True
            else:
                if top >= 0:
                    if bottom < self.height:    # 3
                        pass
                    else:                       # 4
                        pass
                else:                           # 2
                    pass
        else:
            if top >= 0:
                if bottom < self.height:        # 7
                    pass
                else:                           # 6
                    pass
            else:                               # 8
                pass
        return None


    @staticmethod
    def _sanitize_column(column, arg):
        rest = list(filter(lambda p: len(p[0]) and len(p), column))
        if len(rest) != len(column):
            pass
        return rest[0] if len(rest) == 1 else unite_two_arrays(rest, True, arg)


    def sub_array(self, x, y, view):
        # well its Indian a bit
        height, width = view[0] + view[2] + 1, view[1] + view[3] + 1
        top = (y - view[0]) % self.height
        left = (x - view[3]) % self.width
        y_parts = [height] if top + height <= self.height \
            else [self.height - top, height - self.height + top]
        x_parts = [width] if left + width <= self.width \
            else [self.width - left, width - self.width + left]

        if len(y_parts) + len(x_parts) == 2:  # trivial case
            return self._unsafe_sub(left, top, width, height)
        whole_res = []
        cur_x = left
        for x_p in x_parts:
            cur_y = top
            column_res = []
            for y_p in y_parts:
                column_res.append(self._unsafe_sub(cur_x, cur_y, x_p, y_p))
                cur_y = (cur_y + y_p) % self.height
            whole_res.append(column_res[0] if len(column_res) == 1
                             else unite_two_arrays(column_res, True, (x, y, view)))
            # clean = self._sanitize_column(column_res, (x, y, view))
            # if len(clean) > 0:
            #    whole_res.append(clean)
            cur_x = (cur_x + x_p) % self.width
        if len(whole_res) == 1:
            return whole_res[0]
        elif len(whole_res) == 2:
            return unite_two_arrays(whole_res, False, (x, y, view))


    def subarray(self, x, y, deltas):
        nx, ny = x + deltas[0], y + deltas[1]
        if nx >= 0:
            if ny >= 0:  # one part
                self._unsafe_sub(x, y, *deltas)
            else:  # two parts
                pass
        elif ny >= 0:  # two parts
            pass
        else:  # four parts
            pass


w = 100
h = 40
_n_view = [2, 2, 0, 2]

views = gen_views(_n_view)

m = [[*map(lambda x: x + h*i, range(w))] for i in range(h)]
mp = Map(w, h, m)

a = [[[0]*4 for x in range(w)] for y in range(h)]

def f():
    for y in range(h):
        for x in range(w):
            for d in range(4):
                a[y][x][d] = mp.sub_array(x, y, views[d])

def test():
    """Stupid test function"""
    lst = []
    for i in range(100):
        lst.append(i)

def timing(func, count=1):
    t1 = time.time()
    for _ in range(count):
        func()
    t2 = time.time()
    return (t2 - t1)/count

tf2 = timing(test, 100000)
tf1 = round(timing(f, 1), 5)
pass


