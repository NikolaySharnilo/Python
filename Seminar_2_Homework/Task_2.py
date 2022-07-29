# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial(n: int):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

def mult(n, x = []):
    x.append(factorial(n))
    return x

n = int(input("Введите число: "))
for i in range(1, n+1):
    multList = mult (i)

print(f"Произведение чисел от 1 до {n = } -> {multList}")