import random

n = int(input("Введите количество символов:"))
array = list(range(n))
random.shuffle(array)
print(array)

for i in range(n):
    minim = i
    for k in range(minim, n):
        if array[k] < array[minim]:
            minim = k
    if minim != i:
        array[i], array[minim] = array[minim], array[i]

print(array)