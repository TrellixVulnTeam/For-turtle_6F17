import math
def for_5a(n): # Пингвины
    for i in range(n):
        print('  _~_  ',end=' ')
    print(' ')
    for i in range(n):
        print(' (o o) ',end=' ')
    print(' ')
    for i in range(n):
        print(' / V \\ ',end=' ')
    print(' ')
    for i in range(n):
        print('/( _ )\\',end=' ')
    print(' ')
    for i in range(n):
        print(' ^^ ^^ ',end=' ')
    print(' ')
for i in range(10):
    for_5a(i)


def for_6a(n): # Флаги
    for i in range(n):
        print('+___',end=' ')
    print(' ')
    for i in range(n):
        print('|',i+1,' /',sep='',end=' ')
    print(' ')
    for i in range(n):
        print('|__\\',end=' ')
    print(' ')
    for i in range(n):
        print('|   ',end=' ')
    print(' ')
for i in range(10):
    for_6a(i)


def for_5b(n):  # Количество нулей
    n = int(input('Введите количество вводимых букв'))
    i = 0
    b = 0
    while n != i:
        i += 1
        a = int(input('введите букву'))
        if a == 0:
            b += 1
    print('Количество нулей:', b)


def for_6b():  # Замечательные числа
    for i in range(10, 100):
        if i == 2 * (i % 10) * (i // 10):
            print(i)
for_6b() # Ответ 36

def for_7b(n):  # Замечательные числа 2
    for i in range(100, 1000):
        if n == (i // 100) + (i % 10) + ((i // 10) % 10):
            print(i)
for i in (0, 2, 3, 26, 27):
    print(i)
    for_7b(i)


def for_1c(n):  # Лесенка
    a = 0
    for i in range(1, n + 1):
        while a != i:
            a += 1
            print(a, end='')
        a = 0
        print()
for i in range (10):
    for_1c(i)

def for_2c(a, b, c, d, e):  # Диофантово уравнение
    z = 0
    x = 0
    while x < 1000:
        if x == e:
            pass
        elif ((a * (x ** 3)) + (b * (x * x) + (c * x) + d)) / (x - e) == 0:
            z += 1
        x += 1
    return (z)
def for_21c(a, b, c, d, e): # Диофантово уравнение
    count = 0
    for i in range(0,1001):
        if i !=e :
            if ((a * (i) ** 3 + b * (i) ** 2 + i * c + d)/(i-e))==0:
                count += 1
    return (count)
for a in range (-2, 2):
    for b in range(-2, 2):
        for c in range(-2, 2):
            for d in range(-2, 2):
                for e in range(-2, 2):
                    if not for_2c(a, b, c, d, e) == for_21c(a, b, c, d, e):
                        print('Fail', a, b, c, d, e, "Д/б =", for_21c(a, b, c, d, e), "А у тебя", for_2c(a, b, c, d, e))

def for_3c(a, b):  # Замечательные числа
    x = min(a, b)
    y = max(a, b)
    while x <= y:
        if (x % 10) == (x // 1000) and (((x % 100) // 10) == ((x // 100) % 10)):
            print(x)
        x += 1
for_3c(1000, 9999)

def for_4c(a, b):  # Замечательные числа 2
    x = min(a, b)
    y = max(a, b)
    while x <= y:
        c = int(x / 1000)
        d = int(x % 10)
        e = int((x % 100) // 10)
        f = int((x // 100) % 10)
        if (c == d == e and c != f) or (c == d == f and e != f) or (f == d == e and c != f) or (c == f == e and d != f):
            print(x)
        x += 1
for_4c(1000, 9999)

def for_5c(a, b, c, d):  # Остатки
    x = min(a, b)
    y = max(a, b)
    for i in range(((x - c + d - 1) // d * d + c), y + 1, d):
        print(i, '', end='')
for a in ((1, 100, 3, 33),(1, 100, 0, 25),(1, 100, 6, 7),(10, 100, 4, 50),(1, 100, 1, 2)):
    print()
    print(*a, end = "->")
    for_5c(*a)

def for_6c(n):  # Потерянная карточка
    k = 1
    a = 0
    b = 0
    while k != n:
        a += (int(input()))
        k += 1
    for i in range(1, n + 1):
        b += i
    print(b - a)


def for_7c(k):  # Треугольная последовательность
    print(1, end='')
    for i in range(2, k + 1):
        for n in range(i):
            print(',', i, end='', sep='')
    print('.')
for i in range(20):
    print()
    for_7c(i)

def for_8c(n):  # Сумма факториалов
    a = 1
    for i in range(n, 1 - 1, -1):
        a *= i
        a += 1
    return (a - 1)
for i in range(1, 20):
    if not for_8c(i) == sum(math.factorial(j) for j in range(1, i + 1)):
        print('\n Fail!', i, for_8c(i), sum(math.factorial(j) for j in range(i)), end='')