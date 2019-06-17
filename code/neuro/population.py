from Sheelsnwolfes.code.neuro.genotype import Genotype
from Sheelsnwolfes.code.neuro.neuronet import NeuroNet


class Population:
    def __init__(self, net_config, genotypes_count=100, ai_func=None, genotypes=None):
        self.ai_func = ai_func or NeuroNet.create_net_by_config(net_config)
        self.genotypes = genotypes or self.create_random_genotypes(genotypes_count, net_config.get_weights_count())
        self.genotypes_count = genotypes_count


    @staticmethod
    def create_random_genotypes(count, weights_count):
        return [Genotype.make_random_instance(weights_count) for _ in range(count)]











