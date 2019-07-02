resheto = []
p = int(input("Введите границу поиска простых чисел:"))
for i in range(2, p+1):
    resheto.append(i)
print(resheto)
#фОРМИРОВАНИЕ СПИСКА ДО N

k = 0  #Положение элемента простого числа в списке порядка N
while True:
    n = resheto[k] ** 2
    if n > p:
        break
    s = n
    while n <= p:
        resheto.remove(n)
        n += s
    k = k + 1  #Обозначение положение следующего простого числа

print(resheto)
