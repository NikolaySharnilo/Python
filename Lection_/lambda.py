
path = "/Users/user/Desktop/Разработчик/Python/Lection_/text.txt"
with open(path, 'r', encoding='utf-8') as file:
    a = file.read()
    sList = a.split(' ')


sList = list(map(int, sList))
sList = list(filter(lambda x: not x % 2, sList))
sList = list(map(lambda x: (x, x**2), sList))

print(sList)
