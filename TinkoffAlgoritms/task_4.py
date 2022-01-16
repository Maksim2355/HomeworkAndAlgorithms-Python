input = input().split(' ')

size_arr = int(input[0])

arr = input[1::]

# берем максимальные числа, выходящие за границы диапазона​ (1⩽ ai ⩽5).
min = 6
max = 0

indexes_max_items = []

for i in range(size_arr):
    current_item = int(arr[i])
    if current_item <= min:
        min = current_item
    if current_item > max:
        max = current_item
        indexes_max_items.clear()
        indexes_max_items.append(i)
    if current_item == max:
        indexes_max_items.append(i)

# конвертируем число в строку для замены в массиве
value_for_replace = str(min)
for index in indexes_max_items:
    arr[index] = value_for_replace

print(' '.join(arr))
