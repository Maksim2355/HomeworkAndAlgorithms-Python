import os
OS = os.name
if OS == 'nt':
    path = 'C:\\Poisk\\'
elif OS == 'posix':
    path = 'home\\'
while True:
    search_target = input("Введите цель поиска. Вы должны указать расширение, если это файл. Если это папка, то просто название:")

    def recurs_seacrh(path): #Передаем в качестве аргументов основную директорию и уровень вложенности по умолчанию будет равен 1
        for i in os.listdir(path):
            if i == search_target:
                return print(path + '\\' + i)
            elif os.path.isdir(path + '\\' + i):
                recurs_seacrh(path + '\\' + i)
            ыф

    print(recurs_seacrh(path))
