# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def funcCalculation(n):
    result = 0
    for i in range(1, n + 1):
        result = result + ((1 + (1 / i))**i)
    return round(result, 1)


sumList = []
n = int(input("Введите число: "))
for i in range(1, n):
    sumList.append(f"{i}: {funcCalculation(i)}")

print(sumList)

# результат не совпадает с примером потому что формула не ясна в задаче, указал как понял.
# в примере формула: $(1+\frac 1 n)^n$ 