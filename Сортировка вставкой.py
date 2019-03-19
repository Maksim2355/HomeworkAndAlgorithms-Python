array = []
n = int(input("Enter numbers of elements:"))
for i in range(n):
    array.append(int(input("Enter numb")))
print(array)

sortedArray = [array[0]]

for i in range(1, n):
    j = 0
    while j < len(sortedArray) and sortedArray[j] < array[i]:
        j = j + 1
    sortedArray.insert(j, array[i])

print(sortedArray)
