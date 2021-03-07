from random import randint

matrix = []

while True:
    try:
        n = int(input("Введите порядок матрицы: "))
        if n > 0:
            break
    except ValueError:
        print("Некорректный ввод! Введите целое положительное число.")
# ==========================================================================
print("\nМатрица:\n")                                   # Заполнение матрицы
for i in range(n):                                      # и вывод на экран
    matrix.append([])                                   #
    for j in range(n):                                  #
        matrix[i].append(randint(-9, 10))               #
    print("    ", matrix[i])                            #
# ==========================================================================


""" Информация:
        det_matrix - матрицы, детерминат которых будем находить
        matrix_determinant - детерминант матрицы (дополнений матрицы)
        i_string_matrix - номер элемента, для которого составляем дополнение
        j_string_complement - номер строки элемента, который будет записан в дополнение
        k_column_complement - номер столбца элемента, который будет записан в дополнение
        complement_index - нумерация строк дополения """


def determinant(det_matrix):
    matrix_determinant = 0
    if len(det_matrix) == 1:
        return det_matrix[0][0]
    matrix_complement = []
    # ==============================================================================================================================
    for i_string_matrix in range(len(det_matrix)):                                                                      # Вычисляем
        complement_index = 0                                                                                            # дополнения
        for j_string_complement in range(1, len(det_matrix)):                                                           # для
            matrix_complement.append([])                                                                                # каждого
            for k_column_complement in range(len(det_matrix)):                                                          # элемента
                if k_column_complement != i_string_matrix:                                                              # первной
                    matrix_complement[complement_index].append(det_matrix[j_string_complement][k_column_complement])    # строки
            complement_index += 1                                                                                       #
        # ==============================================================================================================================
        if i_string_matrix % 2 == 0:                                                                                       # Подчитываем
            matrix_determinant = matrix_determinant + determinant(matrix_complement) * det_matrix[0][i_string_matrix]      # детерминант
        else:                                                                                                              # для
            matrix_determinant = matrix_determinant - determinant(matrix_complement) * det_matrix[0][i_string_matrix]      # матриц
        matrix_complement = []                                                                                             #
        # ==============================================================================================================================
    return matrix_determinant


print("\nДетерминант матрицы: ", determinant(matrix))