# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def archivate(sourceStr):
    sourceStr = sourceStr + " "  # + " " что бы не терялся последний символ
    archiveStr = ""
    j = 1
    count = 2  # 2 что бы не терялся первый символ
    for i in range(0, len(sourceStr)):
        i = j
        temp = ""
        for j in range(i + 1, len(sourceStr)):
            if sourceStr[i] == sourceStr[j]:
                count += 1
                temp = (f"{count}{sourceStr[i]}")
            elif (len(temp) > 0):
                break
            else:
                temp = (f"{sourceStr[i]}")
                break

        archiveStr = (f"{archiveStr}{temp}")
        count = 1

    return archiveStr


def unArchivate(sourceStr):
    sourceStr = sourceStr
    archiveStr = ""
    for i in range(0, len(sourceStr)):
        if sourceStr[i].isnumeric() == True:
            for j in range(0, int(sourceStr[i])):
                archiveStr = archiveStr + sourceStr[i+1]
        elif sourceStr[i-1].isnumeric() == False:
            archiveStr = archiveStr + sourceStr[i]
    return archiveStr


path = "/Users/user/Desktop/Разработчик/Python/Seminar_5_Homework/Task_4_1.txt"
with open(path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    sourceStr = lines[0]

# print(sourceStr)

archiveStr = archivate(sourceStr)
unArchiveStr = unArchivate(archiveStr)

# print(archiveStr)
# print(unArchiveStr)

with open(path, 'w', encoding='utf-8') as file:
    file.writelines(sourceStr)
    file.writelines(archiveStr)
    file.writelines(unArchiveStr)
