# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

path1 = '/Users/user/Desktop/Разработчик/Python/Seminar_4_Homework/Task_5_1.txt'
path2 = '/Users/user/Desktop/Разработчик/Python/Seminar_4_Homework/Task_5_2.txt'

with open(path1, 'r', encoding='utf-8') as file:
    a1 = file.read()

with open(path2, 'r', encoding='utf-8') as file:
    a2 = file.read()

path3 = '/Users/user/Desktop/Разработчик/Python/Seminar_4_Homework/Task_5_3.txt'
with open(path3, 'a', encoding='utf-8') as file:
    file.writelines(f"{a1} + {a2}")  


