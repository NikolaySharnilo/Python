# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numList = [1.1, 1.2, 3.1, 5, 10.01]
max = numList[0] % 1
min = numList[0] % 1
for i in numList:
    num = i % 1
    if num > max and num > 0:
        max = num
    if num < min and num > 0:
        min = num

print(f" - {numList} => {round(max - min, 3)}")