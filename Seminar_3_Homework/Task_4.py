# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = 45
temp = ""
while n > 1:
    if n // 2 > 0:
        temp = (f"{n - 2 * (n // 2)}{temp}")
        n = int(n // 2)
    if n < 2:
        temp = (f"{n}{temp}")
print(temp)