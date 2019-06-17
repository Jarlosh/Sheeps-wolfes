from Sheelsnwolfes.code.configuration.config import Config
from Sheelsnwolfes.code.tools.tools import calculate_view_size

def str_to_array(attr):
    if attr[0] == '[':
        attr = attr[1:-1]
    return list(map(int, attr.split(',')))


class NeuroConfig(Config):
    north_view = [2, 2, 0, 2]
    trans_layers = None
    in_count = None
    out_count = 1

    type_mapping = {
        'north_view': str_to_array,
        'trans_layers': str_to_array,
        'out_count': int,
        # in_count is not allowed
    }

    def post_init(self):
        self.in_count = self._calculate_in_count(self.north_view)

    @staticmethod
    def _calculate_in_count(north_view):
        width, height = calculate_view_size(north_view)
        return width * height

    def get_north_view(self):
        return self.north_view

    def get_net_parameters(self):
        return self.in_count, \
               self.out_count, \
               self.trans_layers

    def get_weights_count(self):
        return sum(self.trans_layers) + self.out_count



