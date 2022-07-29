# Реализуйте алгоритм перемешивания списка

numList = [1,2,3,4,5]
j = len(numList) -1

for i in range(0, j):
    (numList[i], numList[j]) = (numList[j], numList[i])
    j = j - i
    
print(numList)