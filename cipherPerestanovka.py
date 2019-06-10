import re

letter = re.findall(r'\w', input("Введите послание"))
columns = re.findall(r'\w+', input("Введите порядок столбцов для шифровки "))
lines = re.findall(r'\w+', input("Введите порядок строчек для шифровки "))


cipher = [[] for k in range(len(lines))]
active_line = 0
for k in range(len(letter)):
    if active_line == len(lines):
        active_line = 0
    cipher[active_line].append(letter[k])
    active_line += 1
for i in range(1, len(cipher)):
    len_normal = len(cipher[0])
    if len(cipher[i]) < len_normal:
        cipher[i].append(" ")

#Меняем порядок стобцов и строчек
new_array = []
#Переставляем столбцы
for i in range(len(lines)):
    new_colums = []
    for k in columns:
        new_colums.append(cipher[i][int(k) - 1])
    new_array.append(new_colums)
cipher = []
for i in lines:
    cipher.append(new_array[int(i) - 1])

print(cipher)