from random import randint
array = []
p = int(input("Введите размер масссива:"))
for i in range(p):
    array.append(randint(1,50))
array.sort()
print(array)
element = int(input("Введите число для поиска:"))


def search():
    for i in range(p):
        if array[i] == element:
            return i


if search() == None:
    print("Число не найдено")
else:
    print(search())