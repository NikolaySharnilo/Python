# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from ast import IsNot


def sumNumber(n: str):

    result = 0
    for i in n:
        if i.isnumeric() == True:
            result = result + int(i)
    print(result)

n = input("Введите значения для суммирования: ")
sumNumber(n)

