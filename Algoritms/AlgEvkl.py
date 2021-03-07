increasing_number = int(input("Введите большее число:"))
smaller_number = int(input("Введите меньшее число:"))


while increasing_number != 0 and smaller_number != 0:
    remainder = increasing_number % smaller_number # Остаток
    increasing_number = smaller_number
    smaller_number = remainder
print(increasing_number)
