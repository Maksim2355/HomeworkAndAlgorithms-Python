bin_numb = (input("Введите строку для перевода"))


def bin_to_dec(bin_numb):
    dec_numb = 0
    degree = len(bin_numb) - 1
    for i in bin_numb:
        if i == "1":
            dec_numb = dec_numb + 2 ** degree
        elif i != "0":
            return print("Неверная команда")
        degree = degree - 1
    return print(dec_numb)


bin_to_dec(bin_numb)