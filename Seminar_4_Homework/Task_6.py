# 1. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

path = '/Users/user/Desktop/Разработчик/Python/Seminar_4_Homework/Task_6_1.txt'
with open(path, 'r', encoding='utf-8') as file:
    a = file.read()
    firstList = (a.split('\n'))
# print(firstList)

secondList = []
smallList = []
b = 20000
score = 0
for i in range(len(firstList)):
    secondList.append(firstList[i].split(' '))
    secondList[i][1] = float(secondList[i][1])
    if secondList[i][1] < b:
        smallList.append(secondList[i][0])
    score += secondList[i][1]

print(f"Сотрудники с откладом < 20 тыс. -> {smallList}")
print(f"Средняя зарплата {round(score / len(secondList), 2)}")
