# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
userNumber = input("Введите значение необходимой точности числа pi: ")

if '.' in userNumber:
    a = userNumber.split('.')
elif ',' in userNumber:
    a = userNumber.split(',')

nb_digits = len(a[1]) + 1
print(format(math.pi, '.%dg' % nb_digits))