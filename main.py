import math
n = int(input('Введите число: '))
a = -math.log2(2**-n)
expression = f'{n} = -math.log2(math.log2(math.sqrt({n}**2)))'
print(int(a))
print(expression)
