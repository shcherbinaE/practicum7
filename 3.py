import math
n = int(input('Введите число: '))
while n != math.isqrt(n) ** 2:
    print('Введенное число не является полным квадратом')
    n = int(input('Введите новое число: '))
print('Введенное число является полным квадратом')