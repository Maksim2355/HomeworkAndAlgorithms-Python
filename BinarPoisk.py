from random import randint
array = []
for i in range(15):
    array.append(randint(1,50))
array.sort()
print(array)

element = int(input("Что вы хотите найти?"))
mid = len(array) // 2
end = (len(array) - 1)
low = 0
while element != array[mid] and low <= end:
    if element < array[mid]:
        end = mid - 1
    else:
        low = mid + 1
    mid = (low + end) // 2
if low > end:
    print("Число не найдено")
else:
    print("Номер элемента в списке:", mid)