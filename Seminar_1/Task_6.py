# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
from tracemalloc import stop


n = int(input('Введите число n = '))
if n < 1 or n > 7:
    print("Введены не корректные данные")
    exit()

dictionaryDayList = {1: "Понедельник", 2: "Вторник", 3: "Среда",
                     4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}

if n > 5:
    print(f"Введенный день {dictionaryDayList.get(n)} - выходной")
else:
    print(f"Введенный день {dictionaryDayList.get(n)} - будний")
