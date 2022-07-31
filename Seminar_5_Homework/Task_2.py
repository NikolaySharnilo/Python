# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

def game(count: int, b: int, smart: int ): 
    print(f"Начинает игрок {b}")
    while count > 0:
        player = 0
        if smart != 0:
            if b == 2:
                if count <= 28:
                    player = count
                else:
                    if smart == 2:
                        player = ((count-1) - ((count) // 28) * 28)
                    elif smart == 1:
                        player = int(round(random.uniform(1, 28), 0))
                print(f"Счет {count}. Bot_Игрок {b} делает ход: {player}")
        
        if (smart == 0 or b == 1):
            while (player <= 0 or player > 28 or player > count):
                player = int(
                    input(f"Счет {count}. Игрок {b} введите число до 28: "))

        count -= player

        if count > 0:
            if b == 1:
                b = 2
            else:
                b = 1
    print(f"Победил игрок {b}")


count = 120
firstPlayer = int(round(random.uniform(1, 2), 0))
smart = int(input("Выберите тип игры: 0 - многопользовательский режим, 1 - игра с ботом, 2 - игра с умным ботом: "))
game(count, firstPlayer, smart)

