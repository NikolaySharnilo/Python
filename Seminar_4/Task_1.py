#  работа с файлами

# 1 - with open('/Users/user/Desktop/Разработчик/Python/Seminar_4/test.txt', 'a', encoding='utf-8') as file:
# file.writelines(i)

# file = open('/Users/user/Desktop/Разработчик/Python/Seminar_4/test.txt', 'a', encoding='utf-8')
# file.writelines(i)
# file.close()



# записать в файл цифры от 0 до n
path = '/Users/user/Desktop/Разработчик/Python/Seminar_4/test.txt'
#n = 8
#with open(path, 'a', encoding='utf-8') as file:
#    for i in range(0, n + 1):
#        file.writelines(f"{i}\n")

with open(path, 'r', encoding='utf-8') as file:
    a = file.read()
    strList = a.split()
print(strList)

strList = list(map(int,strList))
print(strList)


#Алгоритм эвклида