array = []
char = int(input("Введите количество символов:"))
for i in range(char):
    array.append(int(input("Введите символ для добавления:")))
print(array)
array_sort = [array[0]]
for i in range(1, char):
    k = 0
    while k < (len(array_sort) - 1):
        if array[i] > array_sort[k]:
            k = k + 1
            continue
        array_sort.insert(k, array[i])
print(array_sort)
