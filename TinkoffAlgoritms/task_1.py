def calculate(value, command):
    if command == '>':
        return value + 1
    elif command == '<':
        return value - 1
    else:
        return value

wizards = {
    'a': 0,
    'b': 0,
    'c': 0
}

condtions = [input(), input(), input()]

for i in condtions:
    # Если вдруг вместо символьных обозначаний будут строки, по типу Рон>Гермиона, то можно строку засплитить
    key = i[0]
    command = i[1]
    wizards[key] = calculate(wizards[key], i[1])

# Сортируем в обратном порядке и сплитим
print(''.join(sorted(wizards.keys(), reverse= True))) 