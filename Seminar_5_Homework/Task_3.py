# Создайте программу для игры в ""Крестики-нолики"".

from ast import IsNot
import random
from tkinter import scrolledtext
from unicodedata import numeric


def checkWin(numList, numPlayer, symbol):

    for i in range(0, 3):  # Проверка строк
        score = 0
        for j in range(0, 3):
            if symbol == numList[i][j]:
                score += 1
        if score == 3:
            congratulation(numList, numPlayer, symbol)
            exit()

    for i in range(0, 3):  # Проверка столбцов
        score = 0
        for j in range(0, 3):
            if symbol == numList[j][i]:
                score += 1
        if score == 3:
            congratulation(numList, numPlayer, symbol)
            exit()

    for i in range(0, 3):  # Проверка первой диагонали
        score = 0
        if symbol == numList[i][i]:
            score += 1
        if score == 3:
            congratulation(numList, numPlayer, symbol)
            exit()

            # Проверка второй диагонали
    score = 1
    if symbol == numList[1][1]:
        score += 1
    if symbol == numList[2][0]:
        score += 1
    if score == 3:
        congratulation(numList, numPlayer, symbol)
        exit()

    score = 9
    for i in range(0, 3):
        for j in range(0, 3):
            if str(numList[i][j]).isnumeric() == False:
                score -= 1
    
    if score == 0:
        print("Игра завершена. Ничья")

    return 0


def congratulation(numList, numPlayer, symbol):
    print(f"Поздравим игрока {numPlayer}, победили {symbol}")
    printList(numList)


def printList(numList):
    for i in range(0, 3):
        print(f"{numList[i][0]}  {numList[i][1]}  {numList[i][2]}", end='\n')


numList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
player1 = ""
temp = False
while temp == False:
    player1 = input(f"Первый игрок, выберите символ 'x' или 'o'(en): ")
    if (player1 == 'x' or player1 == 'o'):
        temp = True

if player1 == 'x':
    player2 = 'o'
else:
    player2 = 'x'

symbol = player1
numPlayer = 1

while True:

    player = 0
    printList(numList)
    while (player <= 0 or player > 9):
        player = int(input(
            f"Игрок {numPlayer}, выберите цифру, соответсвующую ячейке, в которую вы хотите поставить символ {symbol}: "))

    for i in range(0, 3):
        for j in range(0, 3):
            if str(numList[i][j]) == str(player):
                numList[i][j] = str(symbol)
    
    a = checkWin(numList, numPlayer, symbol)

    if symbol == player1:
        symbol = player2
        numPlayer = 2
    else:
        symbol = player1
        numPlayer = 1
