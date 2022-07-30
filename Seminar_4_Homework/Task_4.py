# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = 2
path = '/Users/user/Desktop/Разработчик/Python/Seminar_4_Homework/Task_4_Уравнения.txt'
with open(path, 'a', encoding='utf-8') as file:
    file.writelines(f"{random.randint(0, 100)}*x^{k} + {random.randint(0, 100)}*x + {random.randint(0, 100)} = 0\n")  
    file.writelines(f"{random.randint(0, 100)}*x^{k} + {random.randint(0, 100)} = 0\n") 
    file.writelines(f"{random.randint(0, 100)}*x^{k} = 0\n") 
