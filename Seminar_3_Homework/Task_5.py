# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def unFibonacci(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return unFibonacci(n + 2) - unFibonacci(n + 1)


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Введите число: "))
if n < 0:
    n = -n

numList = []
for i in range(-n, n+1):
    if i < 0:
        numList.append(unFibonacci(i))
    elif i > 0:
        numList.append(fibonacci(i))
    elif i == 0:
        numList.append(0)

print(numList)
