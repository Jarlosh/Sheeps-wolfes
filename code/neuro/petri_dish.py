from Sheelsnwolfes.code.neuro.neuronet import NeuroNet


class PetriDish:
    def __init__(self, sheep_config, wolf_config, genotypes=None):
        self.sheep_ai_func = NeuroNet.create_net_by_config(sheep_config)
        self.wolf_ai_func = NeuroNet.create_net_by_config(wolf_config)
        self.genotypes_count = 100

        if not genotypes:
            pass

    def create_random_genotypes(self, count):
        pass






