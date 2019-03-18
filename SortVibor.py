array = []
char = int(input("Введите количество символов:"))
for i in range(char):
    array.append(int(input("Введите символ для добавления:")))

i = 0
while i < char:
    m = i
    j = i + 1
    while j < char:
        if array[j] < array[m]:
            m = j
        j += 1
    array[i], array[m] = array[m], array[i]
    i += 1
print(array)