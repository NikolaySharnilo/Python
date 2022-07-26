# Показать первую цифру дробной части числа

from posixpath import split

n = input('Введите число N = ').split(',')
print(n[1][:1])


