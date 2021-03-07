matri = [[1, 5, 2],
         [1, 4, 2],
         [4, 2, 0]]
#det = 8
matrix_siz = 3


def minor(matrix, del_str, matrix_size):
    del matrix[del_str]
    for i in range(matrix_size):
        del matrix[i][0]
    print(matrix)
    return matrix


def det(matrix, matrix_size):
    if matrix_size == 1:
        return matrix[0][0]
    elif matrix_size == 2:
        return (matrix[0][0] + matrix[1][1]) - (matrix[0][1] + matrix[1][0])
    else:
        det = 0
        for i in range(matrix_size):
            minor2 = minor(matrix, i, matrix_size - 1)
            det += (1 ** (i + 2)) * matrix[i][0] * matrix(minor2, matrix_size - 1)
        return det


print(det(matri, matrix_siz))