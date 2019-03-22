resheto = []
p = int(input("Введите границу поиска простых чисел:"))
for i in range(2, p+1):
    resheto.append(i)
print(resheto)
#фОРМИРОВАНИЕ СПИСКА ДО N

k = 0  #Положение элемента простого числа в списке порядка N
while k < len(resheto):
    n = resheto[k]
    while n < p:
        s = 2
        n = n * s  #Число, кратное простому числу
        if n not in resheto:  #Проверка наличие удаляемого элемента в списке
            continue
        else:
            resheto.remove(n)  #Удаление числа кратному простому числу
        s = s + 1
    k = k + 1  #Обозначение положение следующего простого числа

print(resheto)
