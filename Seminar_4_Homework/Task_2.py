# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def mult(n):
    numList = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            numList.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        numList.append(n)
    return numList


n = 45
print(f"{n} -> {mult(n)}")
