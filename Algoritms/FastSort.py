import random
n = int(input("Введите количество символов:"))
array = list(range(n))
random.shuffle(array)


def quicksort(array):
    if len(array) <= 1:  #Базовый случай
        return array
    else:  #Рекурсивный случай
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  #Подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot]  #Подмассив всех элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort(array))