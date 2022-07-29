# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.

def sequanceToN(n):
    if n < 0:
        n = -n
    numList = []
    for i in range(-n, n+1):
        numList.append(i)
    return numList


def multPositionList(numList=[], *arg):
    if max(arg) > len(numList) or min(arg) < 0:
        print(f"Некоторые позиции {arg} за пределами диапазона списка")
        exit()

    result = 1
    for i in arg:
        result = result * numList[i]
    print(result)


n = 4
print(sequanceToN(n))
multPositionList(sequanceToN(n), 0, 1, 2)
