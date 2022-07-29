# Напишите программу, в которой пользователь будет задавать две строки
# а программа - определять количество вхождений одной строки в другой

def findingStrInStr(fStr, inStr):
    count = 0
    lenStringToFind = len(inStr)
    for i in range(len(fStr) - lenStringToFind+1):
        if (fStr[i:i+lenStringToFind] == inStr):
            count = count + 1
    print(count)


fStr = input("Введите строку, в которой необходимо найти вхождение: ")
inStr = input("Ведите строку которую необходимо найти: ")
findingStrInStr(fStr, inStr)
