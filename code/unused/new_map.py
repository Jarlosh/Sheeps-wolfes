# def cycle_right_array(arr, i, ):
#     return arr[i:] + arr[:i]
#
#
# def gen_views(north_view):
#     return [cycle_right_array(north_view, -i) for i in range(4)]
#
#
# def cr_array(width, height):
#     return [[0] * width for _ in range(height)]
#
#
# def transpose_map(old_mp):
#     width, height = len(old_mp[0]), len(old_mp)
#     return [[old_mp[y][x] for y in range(height)] for x in range(width)]
#
#
# class Map:
#
#     def __init__(self, width, height, map_array2d):
#         self.mp = map_array2d
#         self.tr_mp = transpose_map(map_array2d)
#         self.width = width
#         self.height = height
#
#     def write_to_mp(self, x, y, val):
#         self.mp[x][y] = val
#         self.tr_mp[y][x] = val
#
#     @staticmethod
#     def unsafe_sub(mp_to_select, x, y, width, height):
#         # method is unsafe: no index checks
#         return [row[x:x + width] for row in mp_to_select[y:y + height]]
#
#     @staticmethod
#     def lazy_unsafe_sub(mp_to_select, x, y, width, height):
#         for row in mp_to_select[y:y + height]:
#             yield row[x: x + width]
#
#     def gen_view_func(self, north_view):
#         # After I wrote it I'm not sure if this realisation actually faster,
#         # I'll check it later --J
#         view_funcs = []
#         views = gen_views(north_view)
#         m_width, m_height = self.width, self.height
#         for view_index in range(len(views)):
#             orientation = 1 if view_index // 2 == 0 else -1
#             if view_index % 2 == 0:  # is vertical?
#                 m_width, m_height = [self.width, self.height]
#                 my_mp = self.mp
#                 kx, ky = [1, -1][::orientation]
#                 def trivial(x, y, width, height):
#                     if width < 0:   # crutch for a while
#                         return self.unsafe_sub()
#
#             else:
#                 m_width, m_height = [self.height, self.width]
#                 my_mp = self.tr_mp
#                 kx, ky = [orientation] * 2
#                 if orientation < 0:
#                     def trivial(x, y, width, height):
#                         pass
#             dx, dy = kx * north_view[3], ky * north_view[0]
#
#             v_width = views[view_index][1] + views[view_index][3] + 1
#             v_height = views[view_index][0] + views[view_index][2] + 1
#
#             def un_func(line_iterators, count):
#                 it1, it2 = line_iterators
#                 return [next(it1) + next(it2) for _ in range(count)]
#
#             def get_directed_view(x, y):
#                 nx = (x + dx) % m_width
#                 ny = (y + dy) % m_height
#                 part_x = [v_width] if nx + -kx * v_width <= m_width \
#                     else [m_width - nx, v_width - (m_width - nx)]
#                 part_y = [v_height] if ny + -ky * v_height <= m_height \
#                     else [m_height - ny, v_height - (m_height - ny)]
#
#                 if len(part_x) + len(part_y) == 2:  # trivial case
#                     trivial(nx, ny, kx * v_width, ky * v_height)  # TODO: avoid use of 'trivial' wrapper
#                     # if orientation > 0:
#                     #    pass
#                     # return self.unsafe_sub(my_mp, nx, ny, kx * v_width, ky * v_height)
#
#                 cur_y = ny
#                 whole_res = []
#                 for p_y in part_y:
#                     cur_x = nx
#                     parts = []
#                     for p_x in part_x:
#                         parts.append(self.lazy_unsafe_sub(my_mp, cur_x, cur_y, p_x, p_y))
#                         cur_x = (cur_x + p_x) % m_width
#                     b = [[*it] for it in parts]
#                     parts = [iter(el) for el in b]
#                     if len(parts) == 2:  # should be refactored later --J
#                         whole_res.append(un_func(parts, p_y))
#                     cur_y = (cur_y + p_y) % m_height
#                 if len(whole_res) == 2:
#                     whole_res = whole_res[0] + whole_res[1]
#                 else:
#                     whole_res = whole_res[0]
#                 return whole_res
#
#             view_funcs.append(get_directed_view)
#         return lambda x, y, direction: view_funcs[direction](x, y)
#
#     def make_view_funcs(self, view):
#         # region 0
#
#         view_funcs = []
#
#         dx, dy = view[3], view[0]
#         my_mp = self.mp
#         m_width, m_height = self.width, self.height
#         v_width = 5
#         v_height = 3
#         kx, ky = -1, -1
#
#         # def unite_func(arrs):
#         #     return [arrs[0][y] + arrs[1][y] for y in range(len(arrs[0]))]
#
#         def un_func(line_iterators, count):
#             it1, it2 = line_iterators
#             return [next(it1) + next(it2) for _ in range(count)]
#
#         # endregion
#         def north(x, y):
#             nx = (x + kx * dx) % m_width
#             ny = (y + ky * dy) % m_height
#
#             part_x = [v_width] if nx + v_width <= m_width \
#                 else [m_width - nx, v_width - (m_width - nx)]
#             part_y = [v_height] if ny + v_height <= m_height \
#                 else [m_height - ny, v_height - (m_height - ny)]
#
#             if len(part_x) + len(part_y) == 2:  # trivial case
#                 return self.unsafe_sub(my_mp, nx, ny, v_width, v_height)
#
#             cur_y = ny
#             whole_res = []
#             for p_y in part_y:
#                 cur_x = nx
#                 parts = []
#                 for p_x in part_x:
#                     parts.append(self.lazy_unsafe_sub(my_mp, cur_x, cur_y, p_x, p_y))
#                     cur_x = (cur_x + p_x) % m_width
#                 b = [[*it] for it in parts]
#                 parts = [iter(el) for el in b]
#                 if len(parts) == 2:  # should be refactored later --J
#                     whole_res.append(un_func(parts, p_y))
#                 cur_y = (cur_y + p_y) % m_height
#             if len(whole_res) == 2:
#                 whole_res = whole_res[0] + whole_res[1]
#             else:
#                 whole_res = whole_res[0]
#             return whole_res
#
#         view_funcs.append(north)
#
#         def get_view(x, y, direction):
#             return view_funcs[direction](x, y)
#
#         return get_view
#
#         # cur_x = nx
#         # whole_res = []
#         # for p_x in part_x:
#         #     cur_y = ny
#         #     parts = []
#         #     for p_y in part_y:
#         #
#         #
#         #         cur_y = (cur_y + p_y) % m_height
#         #     cur_x = (cur_x + p_x) % m_width
#
#     def f(self):
#         pass
#
#
# w = 10
# h = 10
# _n_view = [2, 2, 0, 2]
#
# # views = gen_views(_n_view)
#
# m = [[*map(lambda x: x + h * i, range(w))] for i in range(h)]
# mp = Map(w, h, m)
#
# nvf = mp.gen_view_func(_n_view)
#
# a = nvf(5, 5, 3)
# pass
"""
There is a nice idea but I made a lot major mistakes, TODO: implement fast sub_array
--Jarl
"""
