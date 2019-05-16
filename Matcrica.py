from random import randint
matrix_size = int(input("Введите размер матрицы:"))


def column_formation(): #Формирование столбца
    cher = matrix_size
    array = []
    for i in range(cher):
        array.append(randint(0, 25))
    return array


#Формирование матрицы
matrix = []
for i in range(matrix_size):
    matrix.append(column_formation())
print(matrix)


def minor(strokaudalenia, matrix):
    del matrix[strokaudalenia]
    for k in range(len(matrix)):
        del matrix[k][0]
    return matrix


def determinant(matrix, matrix_size):
    if matrix_size == 1:
        return matrix[0][0]
    elif matrix_size == 2:
        det = ((matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1]))
        return det
    else:
        det = 0
        for j in range(matrix_size):
            det = det + ((-1)**(2 + i)) * matrix[j][0] * determinant(minor(j, matrix), matrix_size - 1)
        return det


print(determinant(matrix, matrix_size))
