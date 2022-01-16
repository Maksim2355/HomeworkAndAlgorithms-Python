map_keyboard = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

# преобразует символ в нужный код на клавиатуре
def calculate(char):
    for key, value in map_keyboard.items():
        if char in value:
            return key * (value.index(char) + 1)
    return ""

count_ministries = int(input())
count_char_ministries = 7

# массив полученных значений ввода
arr_inputs = []

# массив для расширофки кода этих самых значений
arr_codes = []

for i in range(count_ministries):
    arr_inputs.append(input())

for items in arr_inputs:
    arr1 = ""
    for k in range(count_char_ministries):
        arr1 += calculate(items[k])
    arr_codes.append(arr1)

min_index = len(min(arr_codes))

count_non_unuqie = set()

print("________________")
print(arr_codes)
print("________________")

for current_postion in range(min_index):
    for index in range(len(arr_codes) -1):
        if arr_codes[index][current_postion] == arr_codes[index + 1][current_postion]:
            print(arr_codes[index][current_postion])
            print(arr_codes[index + 1][current_postion])
            count_non_unuqie.add(index) 
            count_non_unuqie.add(index + 1) 

print(count_non_unuqie)
print(len(count_non_unuqie))
count_ministries -= len(count_non_unuqie)

print(count_ministries)
