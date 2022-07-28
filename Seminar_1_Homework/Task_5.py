# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def inputNumbers(x):
    Point = ["A (x)", "A (y)", "B (x)", "B (y)"]
    a = []
    for i in range(x):
        a.append(int(input(f"Введите значение {Point[i]}: ")))
    return a


Coord = inputNumbers(4)  # 4 - count coordinates

result = round(((Coord[2] - Coord[0])**2 + (Coord[3] - Coord[1])**2)**0.5, 2)

print(f"- A ({Coord[0]}, {Coord[1]}); B ({Coord[2]}, {Coord[3]}) -> {result}")
