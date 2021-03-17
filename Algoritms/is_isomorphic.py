import numpy as np
from itertools import permutations

matrix_size = 3


def is_isomorphic(matrix1, matrix2, perm):
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix1[i][j] != matrix2[perm[i]][perm[j]]:
                return False
    return True


graph_1 = np.array(
    [[0, 1, 1],
     [1, 0, 0],
     [1, 0, 0]]
)
graph_2 = np.array(
    [[0, 0, 1],
     [0, 0, 1],
     [1, 1, 0]]
)

p = permutations([i for i in range(matrix_size)])


for k in p:
    if is_isomorphic(graph_1, graph_2, k):
      print("True")
      break
