import pickle
import gzip

import numpy as np


def load_data():
    f = gzip.open('../data/mnist.pkl.gz', 'rb')
    training_data, test_data, _ = pickle.load(f, encoding="latin1")
    f.close()
    return training_data, test_data


def load_data_wrapper():
    tr_d, va_d = load_data()
    training_inputs = [x for x in tr_d[0]]
    training_results = [y for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    validation_inputs = [x for x in va_d[0]]
    validation_results = [y for y in va_d[1]]
    validation_data = (validation_inputs, validation_results)
    return training_data, validation_data, 784


def vectorized_result(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e
