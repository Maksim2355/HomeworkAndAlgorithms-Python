size_arr = int(input())

arr = input().split(' ')

can_arr_non_decreasing = True

for i in range(size_arr - 1):
    value_1 = int(arr[i])    
    value_2 = int(arr[i + 1])

    if value_2 < value_1:
        if (-value_1) <= value_2:
            arr[i] = str(-value_1)
        elif (-value_2) >= value_1:
            arr[i + 1] = str(-value_2)
        else:
            can_arr_non_decreasing = False
            break

if can_arr_non_decreasing:
    print("Yes")
    print(" ".join(arr))
else:
    print("No")

