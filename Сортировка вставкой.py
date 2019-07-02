import random
n = int(input("Введите количество символов:"))
array = list(range(n))
random.shuffle(array)

sortedArray = [array[0]]
for i in range(1, n):
    j = 0
    while j < len(sortedArray) and sortedArray[j] < array[i]:
        j = j + 1
    sortedArray.insert(j, array[i])

print(sortedArray)
