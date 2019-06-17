# it's not a cool solution as names could be changed
from Sheelsnwolfes.code.configuration.config import Config
from Sheelsnwolfes.code.tools.tools import concat_arrays, split_for_directions

EMPTY = 0
WOLF = 12
SHEEP = 24
GRASS = 36

class GameConfig(Config):
    sheeps = 100
    wolfes = 100
    grass = 100

    width = 100
    height = 100

    type_mapping = {
        'sheeps': int,
        'wolfes': int,
        'grass': int,
        'width': int,
        'height': int
    }



    def get_wh_size(self):
        return self.width, self.height

    def get_creatures_counts(self):
        return [self.sheeps, self.wolfes]

    def get_objects_counts(self):
        non_creatures = [self.grass]
        return self.get_creatures_counts() + non_creatures

    def make_map_ethalone(self):
        width, height = self.get_wh_size()
        object_counts = self.get_objects_counts()
        sheep_c, wolf_c, grass_c = object_counts
        total_objects = sum(object_counts)
        area = width * height
        ethalone = concat_arrays([
            split_for_directions(WOLF, wolf_c),
            split_for_directions(SHEEP, sheep_c),
            [GRASS] * grass_c,
            [EMPTY] * (area - total_objects)
        ])
        return ethalone


