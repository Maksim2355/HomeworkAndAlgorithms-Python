from random import randint
array = []
p = int(input("Введите размер масссива:"))
for i in range(p):
    array.append(randint(1,100))
print(array)


def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort(array))