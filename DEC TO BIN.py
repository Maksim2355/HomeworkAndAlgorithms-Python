
dec_numb = int(input("Введите свое десятичное число"))

def DEC_TO_BIN(numb):
    remainder = numb % 2
    whole_part = numb // 2
    if whole_part > 0:
        DEC_TO_BIN(whole_part)
    print(remainder)

DEC_TO_BIN(dec_numb)