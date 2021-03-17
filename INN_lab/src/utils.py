import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def activation_neutron(x):
    if sigmoid(x) < 0.5:
        return 0
    else:
        return 1


def clamp(value, min_v, max_v):
    if value < min_v:
        return min_v
    elif value > max_v:
        return max_v
    else:
        return value
