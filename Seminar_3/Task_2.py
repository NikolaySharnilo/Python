
# 2. Напишите программу, которая определить позицию второго вхождения строки в списке либо сообщит, что ее нет.
# - список: ['qwe', 'asd', 'zxc', 'qwe', 'ertye'], ищем: "qwe", ответ: 3

strList = ['qwe', 'asd', 'zxc', 'qwe', 'f', 'ertye']
f = "qwe"
score = 2
for i in range(0, len(strList)):
    if f in strList[i]:
        score -= 1
        if score == 0:
            print(i)
            exit()
    if i == len(strList)-1:
        print(-1)
