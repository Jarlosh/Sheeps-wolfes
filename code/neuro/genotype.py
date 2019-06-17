from Sheelsnwolfes.code.tools.tools import random_values


class Genotype:
    def __init__(self, weights):
        self.weights = weights


    @staticmethod
    def make_random_instance(weights_count):
        weights = random_values(weights_count)
        return Genotype(weights)




