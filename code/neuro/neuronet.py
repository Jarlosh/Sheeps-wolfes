import math

from Sheelsnwolfes.code.tools.tools import random_values


def sigmoid(x):
    return 1 / (1 + math.e**(-x))

def ev(vector, weights, count):
    return sigmoid(sum((vector[i] * weights[i] for i in range(count))))

def lazy_ev(vector, weight_iter):
    return sigmoid(sum((v * w for v, w in zip(iter(vector), weight_iter))))

class NeuroNet:
    @staticmethod
    def create_neuro_func(in_count, out_count, trans_layers):
        tr_count = len(trans_layers)
        layers = trans_layers + [out_count]

        def neuronet(vector, weights):
            wit = iter(weights)
            prev_count = in_count
            for i in range(tr_count + 1):
                nv = []
                for j in range(layers[i]):
                    nv.append(lazy_ev(vector, (next(wit) for _ in range(prev_count))))
                vector = nv
                prev_count = layers[i]
            return vector
        return neuronet

    @staticmethod
    def create_net_by_config(neuro_config):
        return NeuroNet.create_neuro_func(*neuro_config.get_net_parameters())




# region config
view = [2, 2, 0, 2]
# _in_count = (view[0] + view[2]) * (view[1] + view[3])
_in_count = 3
_trans_layers_counts = [2, 2]
_out_count = 1
# _weights = [
#     [[1]*3, [1]*3],
#     [[2]*2, [2]*2],
#     [[3]*2]
#     ]
_weights = random_values(12)
config = (_in_count, _out_count, _trans_layers_counts, _weights)
# endregion
nn = NeuroNet.create_neuro_func(*config)

