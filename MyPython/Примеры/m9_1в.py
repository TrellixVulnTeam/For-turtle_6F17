# Пример 1
from random import *
# Генерация списка
m = [randint(-5,6) for i in range(5)]
# Вывод списка в целом
print(m)
# Вывод списка поэлементно
a,b = 0,0
for i in m:
    if i>=0: a += i
    else:    b += i
print('Сумма положительных: %d, отрицательных: %d' % (a,b))

