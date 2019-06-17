import random

from Sheelsnwolfes.code.tools import bench
from Sheelsnwolfes.code.configuration.game_config import GameConfig
from Sheelsnwolfes.code.tools.tools import cycle_right_array




def gen_views(north_view):
    return [cycle_right_array(north_view, -i) for i in range(4)]


def unite_two_arrays(parts, is_vertical):
    if is_vertical:
        return parts[0] + parts[1]
    else:
        return [parts[0][y] + parts[1][y] for y in range(len(parts[0]))]


class Map:
    def __init__(self, width, height, mp_arr):
        self.mp = mp_arr
        self.width = width
        self.height = height

    @staticmethod
    def create_instance(config=None, ethalone=None):
        if not config:
            config = GameConfig()  # default
        if not ethalone:
            ethalone = config.make_map_ethalone()
        width, height = config.get_wh_size()
        map_array = Map._make_map_array(ethalone, width, height)
        return Map(width, height, map_array)

    @staticmethod
    def _make_map_array(ethalone, width, height):
        values = ethalone  # could copy it but guess its ok to modify
        random.shuffle(values)
        i_iter = iter(values)
        return [[next(i_iter) for _ in range(width)] for _ in range(height)]


    # region sub_array()
    def _unsafe_sub(self, x, y, dx, dy):
        # we mean what x, y, dx, dy >= 0
        # and x + dx < width, y + dy < height
        return [row[x:x + dx] for row in self.mp[y:y + dy]]

    def sub_array(self, x, y, view):
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
                             else unite_two_arrays(column_res, True))
            # clean = self._sanitize_column(column_res, (x, y, view))
            # if len(clean) > 0:
            #    whole_res.append(clean)
            cur_x = (cur_x + x_p) % self.width
        if len(whole_res) == 1:
            return whole_res[0]
        elif len(whole_res) == 2:
            return unite_two_arrays(whole_res, False)
    # endregion

    # region gen_view_func()

    @staticmethod
    def gen_view_func(map_instance, north_view):
        # There is a better implementation idea in 'unused',
        # but I had not enough time to finish, so I finished this crutch
        # --Jarl
        all_views = gen_views(north_view)
        v_width = north_view[1] + 1 + north_view[3]
        v_height = north_view[0] + 1 + north_view[2]
        args = [[v_height, None], [v_width, v_height - 1], [v_height - 1, None], [v_width - 1, v_height]]
        vector_funcs = [Map._wrap_view_func(v_index, args[v_index]) for v_index in range(4)]

        def get_view_vector(x, y, direction_index):
            view = map_instance.sub_array(x, y, all_views[direction_index])
            return vector_funcs[direction_index](view)

        return get_view_vector

    @staticmethod
    def _wrap_view_func(v_index, args):
        # region merge 2d array to vector
        arg0, arg1 = args
        if v_index == 0:
            def view_wrapper(arr):
                result = []
                for y in range(arg0):
                    result += arr[y]
                return result

        elif v_index == 2:
            def view_wrapper(arr):
                result = []
                for y in range(arg0, -1, -1):
                    result += arr[y][::-1]
                return result

        elif v_index == 1:
            def view_wrapper(arr):
                result = []
                for x in range(arg1, -1, -1):
                    for y in range(arg0):
                        result.append(arr[y][x])
                return result

        else:
            def view_wrapper(arr):
                result = []
                for x in range(arg1):
                    for y in range(arg0, -1, -1):
                        result.append(arr[y][x])
                return result
        # endregion
        return view_wrapper
    # endregion











# region benchmark
def _view_all(args):
    h, w, v_func = args
    for y in range(h):
        for x in range(w):
            for d in range(4):
                r = v_func(x, y, d)


def bench_it(w=100, h=100, count=10**2, north_view=None):
    if not north_view:
        north_view = [2, 2, 0, 2]
    m = [[*map(lambda x: x + h * i, range(w))] for i in range(h)]
    mp = Map(w, h, m)

    v_func = mp.gen_view_func(mp, north_view)
    t = bench.bench_func(_view_all, count, (h, w, v_func))
    return round(t * count, 3), round(t, 7)
# endregion
