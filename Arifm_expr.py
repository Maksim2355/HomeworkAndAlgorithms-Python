import re

expr = input("Введите выражение:")
expr = re.findall(r'\S+',expr)
print(expr)
operand1 = ['+', '-']
operand2 = ['*', '/']

