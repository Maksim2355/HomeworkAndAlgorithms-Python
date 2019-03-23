from random import randint
array = []
p = int(input("Введите размер масссива:"))
for i in range(p):
    array.append(randint(1,50))
print(array)  #Полученный рандомный массив


def merge_sort(array):  #Процесс разбиение списка
    if len(array) <= 1:  #Если элемент в списке 1, то сортировка закончена
        return array
    middle = int(len(array) / 2)  #Переменная для разбиение массива на правую и левую часть
    left = merge_sort(array[:middle])  #Левая часть массива
    right = merge_sort(array[middle:])  #Правая часть массива
    return merge(left, right)


def merge(left, right):
    result = []  # Результат сложения
    while len(left) > 0 and len(right) > 0: #До тех пор, пока массивы не буду пустыми
        if left[0] <= right[0]:  # Если элемента из левой части списка меньше, то добавляем в результат и удаляем первый элемент
            result.append(left[0])
            left = left[1:]
        else: #Аналогично для правой части
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:  # Если левый или правый список пустой, то добавляем оставшиеся элементы из непустого списка
        result += left
    if len(right) > 0:
        result += right
    return result

array_sort = merge_sort(array)

print(array_sort)