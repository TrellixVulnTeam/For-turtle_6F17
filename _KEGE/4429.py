'''
№ 4429 (Е. Драчева)
Набор данных состоит из групп натуральных чисел, каждая группа записана в отдельной строке.
В любой группе содержится не менее двух чисел. Из каждой группы выбрали два числа и нашли
их наименьшее общее краткое (НОК). Затем все полученные таким образом значения НОК сложили.
Определите наибольшую сумму, кратную числу 5 или 7 (но не одновременно двум этим числам),
которая может быть получена таким образом.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит
в первой строке количество чисел N (2 ≤ N ≤ 100000). В каждой из следующих N строк файлов
записан сначала размер группы K (N <= 10), а затем – K натуральных чисел, не превышающих 500.
Пример входного файла:
4
2 8 6
3 2 7 8
2 6 5
4 7 3 8 6
Для указанных входных данных значения НОК
для первой группы – 24;
для второй группы – 14, 8, 56;
для третьей группы – 30,
для четвёртой группы – 6, 21, 24, 24, 42, 56.
Значением искомой суммы должно быть число 110 (24+14+30+42).
В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.

'''
from itertools import combinations


def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def NOK(a, b):
    return (a * b) // nod(a, b)


def summing(a: list, b: set):
    aux = [0]*35
    for i in a:
        for j in b:
            if aux[(i + j) % 35] < i + j:
                aux[(i + j) % 35] = i + j
    return aux


file = open('27-77a.txt', 'r')

temp = file.readline()
matrix = []

for i in file:
    aux = [int(j) for j in i.split()]
    matrix.append([aux[i] for i in range(1, len(aux))])

noks = []
for j in matrix:
    aux = [i for i in combinations(j, 2)]
    temp = []
    for i in aux:
        temp.append(NOK(i[0], i[1]))
    noks.append(set(temp))

temp = [0]
for i in noks:
    temp = summing(temp, i)


temp = sorted(temp, reverse=True)
for i in temp:
    if ((i % 5 == 0) or (i % 7 == 0)) and (i % 35 != 0):
        print(i)
        break
