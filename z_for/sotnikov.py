import math


def for_6(n):# Замечательные числа
    for i in range(10,100):
        a=i//10
        b=i%10
        c=2*a*b
        if c==i:
            print(i,sep=' ')
for_6(2)


def for_7b(n):  # Замечательные числа 2
    for i in range(100, 1000):
        a = i // 100
        b = i % 100 // 10
        c = i % 10
        d = a + b + c
        if d == n:
            print(i, sep='')

for i in (0, 2, 3, 26, 27):
    print(i)
    for_7b(i)


def for_1c(n):  # Лесенка
    for i in range(n):
        for i in range(1, i + 2):
            print(i, end='')
        print()

for i in range (10):
    for_1c(i)

def for_2c(a, b, c, d, e):  # Диофантово уравнение
    for x in range(1001):
        s = 0
        if x != e:
            if a * x * x * x + b * x * x + c * x + d == 0:
                s = s + 1
    return (s)
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
    for i in range(a, b):
        c = i // 100 // 10
        d = i // 100 % 10
        e = i % 100 // 10
        f = i % 100 % 10
        if c == f and d == e:
            print(i, sep=' ')
for_3c(1000, 10000)


def for_4c(a, b):  # Замечательные числа 2
    for i in range(a, b):
        c = i // 100 // 10
        d = i // 100 % 10
        e = i % 100 // 10
        f = i % 100 % 10
        if c == d == e or c == d == f or c == e == f or d == e == f:
            print(i, sep=' ')
for_4c(1000, 10000)


def for_5c(a, b, c, d):  # Остатки
    x = ' '
    for i in range(a, b + 1):
        x += str(i) * (i % d == c) + ' '
    print(x)
for a in ((1, 100, 3, 33),(1, 100, 0, 25),(1, 100, 6, 7),(10, 100, 4, 50),(1, 100, 1, 2)):
    print()
    print(*a, end = "->")
    for_5c(*a)

def for_6c(n, l):  # Потерянная карточка
    sum = 0
    for i in range(1, n + l):
        sum += i - 2
    for i in range(n - l):
        sum -= int(input())
    print(sum)


def for_7c(k):  # Треугольная последовательность
    x = 1
    for i in range(1, k + 1):
        print(x, sep='  ')
        if i == x * (x + 1) // 2:
            x += 1



def for_8c(n):  # Сумма факториалов
    x = 1
    y = 1
    for i in range(2, n + 1):
        y += x * i
        x *= i
    return (y)
for i in range(1,20):
    if not for_8c(i) == sum(math.factorial(j) for j in range(1, i+1)):
        print('\n Fail!', i, for_8c(i), sum(math.factorial(j) for j in range(i)), end='')
