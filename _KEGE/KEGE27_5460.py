"""
(№ 5460) (Е. Джобс) Два грузовика собирают мусор на кольцевой автодороге. Известно, что грузовики заезжают на кольцевую
автодорогу и съезжают с неё в одном из пунктов приема мусора. Грузовики движутся по дороге в противоположных
направлениях, собирая мусор во всех пунктах приема мусора, через которые построен их маршрут. Мусор, находящийся в
пунктах, где грузовики заезжают и съезжают с кольца, полностью забирает одна из машин. Пункты приема мусора
располагаются на расстоянии 1 км друг от друга.
Грузовики имеют одинаковую грузоподъемность. Найдите минимальную необходимую грузоподъемность грузовиков, при которой
они могут собрать весь мусор на кольцевой автодороге. Для этого варианта определите минимальное из расстояний, которые
проедут по кольцевой дороге грузовики с найденной грузоподъемностью.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых в первой строке содержит число
N(1 ≤ N ≤ 10 000 000) – количество пунктов сбора мусора на кольцевой автодороге. В каждой из следующих N строк находится
натуральное число, не превышающее 1000 – количество мусора в контейнере. Числа указаны в порядке расположения
контейнеров на автомагистрали, начиная с первого километра.
Пример входного файла :
6
8
20
5
13
7
19
При таких исходных данных один грузовик может собрать мусор в пунктах со 2 по 4 (20+5+13 = 38),
второй в пунктах 1, 6, 5 (8+19+7 = 34).
В этом случае минимальная грузоподъемность составит 38 единиц, а длина маршрута – 2 км: от п. 2 до п. 4
(грузовик заезжает в п. 2 и съезжает с трассы в п. 4) или от п. 1 до п. 5. Ответ: 2.
В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.
"""

file = open('27-5460b.txt')
aux = list(map(int, file.readlines()))[1:]
file.close()
sum_fool = sum(aux)

a = {}
for i in range(len(aux)):
    a[i+1] = aux[i]


l, r, = 1, 1
truck1, truck2 = 0,0
temp = []
diff_min = sum_fool
loop = True
length = len(a)
truck_max = 0
path_min = ()

for _ in range(length):
    while truck1 * 2 <= sum_fool:
        truck1 += a[r]
        try:
            r += 1
            x = a[r]
        except:
            r = 1
            loop = not True

    truck2 = sum_fool - truck1
    diff = abs(truck1 - truck2)

    if loop:
        path1 = r - l - 1
    else:
        path1 = length - abs(r-l) - 1
    path2 = length - path1 - 2

    if diff < diff_min:
        diff_min = diff
        path_min = (min(path1, path2),)


    if diff == diff_min:
        path_min += (min(path1, path2),)

    truck1 -= a[l]
    l += 1

print(min(path_min), diff_min)




