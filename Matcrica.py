from random import randint
matrix_size = int(input("Введите размер матрицы:"))


def column_formation(): #Формирование столбца
    cher = matrix_size
    array = []
    for i in range(cher):
        array.append(randint(0,99))
    return array


#Формирование матрицы
matrix = []
for i in range(matrix_size):
    matrix.append(column_formation())
print(matrix)


#Поиск минора элемента
def minor_extra(strokaudalenia, matrix_size, minor):
    del minor[strokaudalenia]
    for k in range(matrix_size - 2):
        del minor[k][0]
    return det(minor, matrix_size - 1)


#Нахождение определителя
def det(matrix, matrix_size):

    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        det2x2 = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
        return det2x2
    else:
        detMatrix = 0
        for j in range(matrix_size):
            detMatrix = detMatrix + ((-1) ** (j+2)) * matrix[j][0] * minor_extra(j, matrix_size, matrix)
        return detMatrix


print(det(matrix, matrix_size))

