# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
path = "/Users/user/Desktop/Разработчик/Python/Seminar_5_Homework/Task_1_1.txt"
with open(path, 'r', encoding='utf-8') as file:
    a = file.read()
    sList = a.split(' ')

print(sList)
s = "абв"
outList = []
for i in sList:
    if s not in i:
        outList.append(i)
        
print(outList)