# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

path = '/Users/user/Desktop/Разработчик/Python/Seminar_4_Homework/Task_7_1.txt'
with open(path, 'r', encoding='utf-8') as file:
    a = file.read()
    firstList = (a.split('\n'))
firstList = list(map(int, firstList))
print(firstList)

for i in range(0, len(firstList)-1):
    if firstList[i] + 1 != firstList[i+1]:
        print(
            f"Условие A[i] - 1 = A[i-1] не выполняется для числа: {firstList[i]+1}")
