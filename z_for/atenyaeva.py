import math


def for_1a(a, b):
    for i in range(a,b+1):
        print(i,end=' ')


def for_3a(n): # Сумма кубов
    a=0
    for i in range(1,n+1):
        a+=i**3
    return (a)
for i in range (10):
    if sum(j**3 for j in range(1, i+1)) == for_3a(i):
        print('Ok')
    else:
        print(sum(j**3 for j in range(1, i+1)), for_3a(i))

def for_2b(a, b): # Чётные числа
    for i in range(a,b,2):
        c=i%2+i
        print(c)


def for_4b(): # Сумма десяти чисел
    n=0
    for i in range(10):
        a=int(input())
        n+=a
    print(n)


def for_5b(n): # Количество нулей
    for i in range(n):
        if int(input())!= 0:
            n-= 1
    print(n)


def for_1c(n):  # Лесенка
    for i in range(1, n + 1):
        for a in range(1, i + 1):
            print(a, end='')
        print()
for i in range (10):
    for_1c(i)

def for_2c(a, b, c, d, e):  # Диофантово уравнение
    l = 0
    for i in range(0, 1001):
        if i != e:
            if (a * i ** 3 + b * i ** 2 + c * i + d) / (i - e) == 0:
                l = l + 1
        else:
            break
    return (l)
def for_21c(a, b, c, d, e): # Диофантово уравнение
    count = 0
    for i in range(0,1001):
        if (i-e) != 0:
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
    for i in range(a // 100, 100):
        n = i * 100 + i % 10 * 10 + i // 10
        if n >= a:
            if n <= b:
                print(n)
            else:
                break
for_3c(1000, 9999)

def for_4c(a, b):  # Замечательные числа 2
    for i in range(a, b):
        i1 = i // 1000
        i2 = i // 100 % 10
        i3 = i // 10 % 10
        i4 = i % 10
        if (i1 == i2) and (i2 == i3) and (i3 != i4) or (i1 == i2) and (i2 == i4) and (i4 != i3) or (i1 == i3) and (
                i3 == i4) and (i4 != i2) or (i2 == i3) and (i3 == i4) and (i4 != i1):
            print(i)
for_4c(1000, 9999)

def for_5c(a, b, c, d):  # Остатки
    e = (a - c + d - 1) // d * d + c
    for i in range(e, b + 1, d):
        print(i, end=' ')
for a in ((1, 100, 3, 33),(1, 100, 0, 25),(1, 100, 6, 7),(10, 100, 4, 50),(1, 100, 1, 2)):
    print()
    print(*a, end = "->")
    for_5c(*a)

def for_6c(n):  # Потерянная карточка
    z = 0
    for i in range(1, n + 1):
        z += i
    for i in range(n - 1):
        z -= int(input())
    print(z)


def for_7c(k):  # Треугольная последовательность
    l = 1
    n = 0
    for i in range(k):
        print(l, end=' ')
        n += 1
        if n == l:
            n = 0
            l += 1
for i in range(20):
    print()
    for_7c(i)

def for_8c(n):  # Сумма факториалов
    a = 1
    b = 0
    for i in range(1, n + 1):
        a = a * i
        b += a
    return (b)
for i in range(1,20):
    if not for_8c(i) == sum(math.factorial(j) for j in range(1, i+1)):
        print('\n Fail!', i, for_8c(i), sum(math.factorial(j) for j in range(i)), end='')