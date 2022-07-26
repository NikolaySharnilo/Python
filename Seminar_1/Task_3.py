# Вывести на экран числа от -N до N
N = int(input('Введите число N = '))

if N < 0:
    N = -N
for i in range(-N, N+1):
    print(i)

