import random
n = int(input("Введите количество символов:"))
array = list(range(n))
random.shuffle(array)
print(array)

array_sort = [array[0]]
for i in range(1, n):
    length = len(array_sort)
    for k in range(length + 1):
        if k == length:
            array_sort.append(array[i])
        elif array[i] <= array_sort[k]:
            array_sort.insert(k, array[i])
            break


print(array_sort)