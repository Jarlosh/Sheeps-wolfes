from Sheelsnwolfes.code.game_stuff.game_map import Map


class Game:
    def __init__(self, sheep_ai, wolf_ai, config, ethalone=None):
        self.sheep = sheep_ai
        self.wolf = wolf_ai
        self.config = config
        self.map_as_array = Map.create_instance(config, ethalone)

        self.is_over = False


    def make_step(self):
        pass


    def update_state(self):
        pass  # game should be ended?


    def play_until_end(self):
        while not self.is_over:
            self.make_step()
            self.update_state()













