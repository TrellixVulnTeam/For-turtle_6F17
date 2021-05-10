def while_1a(n):  # Список квадратов
    i = 1
    while i ** 2 <= n:
        c = i ** 2
        print(c, end=' ')
        i = i + 1


def while_2a(n):  # Минимальный делитель
    i = 2
    while n % i != 0:
        i += 1
    print(i)


def while_7a():  # Сумма последовательности
    c = 0
    n = 1
    while n != 0:
        n = int(input())
        c = c + n
    print(c)


def while_1b():  # Среднее значение
    r = -1  # количество цифр в последовательности
    c = 0  # summ
    n = 1
    while n != 0:
        n = int(input())
        r += 1
        c = c + n
    print(c / r)


def while_2b():  # Маесимум поседовательности
    i = 0
    n = 1
    while n != 0:
        n = int(input())
        if n > i:
            i = n
    print(i)


def while_1c(n):  # Числа Фибоначи
    i = 0
    a1 = 0
    a2 = 1
    a3 = 0
    if n == 1:
        while i in range(0, n):
            a3 = 1
            i += 1
    elif n > 1:
        while i in range(0, n - 1):
            i += 1
            a3 = a1 + a2
            a1 = a2
            a2 = a3
    print(a3)
for i in (3, 6, 10, 12):
    while_1c(i)

def while_2c(n):  # Номер числа Фибоначи
    def ch(n):
        i = 0
        a, b = 0, 1
        while b <= n:
            i += 1
            a, b = b, a + b
            if a == n:
                return i
        return -1
    print (ch(n))
for i in (2, 8, 10, 55, 144):
    while_2c(i)

def while_3c(a, b):  # Исполнитель "Раздвоитель
    while a != b and a > b:
        if a - b in range(0, b + 1):
            print(-1)
            a = a - 1
        else:
            if a % 2 == 1:
                print('-1')
                a = a - 1
            elif a % 2 == 0:
                print(':2')
                a = a / 2
for i in ((10, 5), (19, 2), (17, 3), (4,3)):
    print(*i, '->')
    while_3c(*i)

def while_4c():  # Максимальное число идущих подряд элементов
    a = 0
    c = 0
    n1 = 0
    n = int(input())
    while n != 0:
        if n1 == n:
            c += 1
        else:
            n1 = n
            a = max(a, c)
            c = 1
        n = int(input())
    a = max(a, c)
    print(a)
for i in range(3):  # 1,2,2,3,3,3,2,2,2,2,1 = 4; 1,2,3,2,1 = 1; 1,9,6,5,5,5,3,4 = 3
    while_4c()


def while_5c():  # Максимальная длинна монотонного фрагмента
    maxim = 0
    c = 0
    n1 = 0
    n = int(input())
    while n != 0:
        if n1 < n:
            while n1 < n and n != 0:
                n1 = n
                c += 1
                n = int(input())
                maxim = max(maxim, c)
        elif n1 > n:
            while n1 > n and n != 0:
                n1 = n
                c += 1
                n = int(input())
                maxim = max(maxim, c)
        c = 1
        if n != 0:
            n = int(input())
        print(c)
    maxim = max(maxim, c)
    print(maxim)
for i in range(3):  # 1,2,3,4,5,6 = 6; 3,2,1,2 = 3; 3,2,1,2,3,4,5,6 = 6
    while_5c()


def while_6c():  # Количество локальных максимумов
    k = 0
    n1 = 0
    n = int(input())
    while n != 0:
        n1 = n
        n = int(input())
        n2 = n
        if n > n1 and n != 0:
            n = int(input())
        if n2 > n and n != 0:
            k += 1
    print(k)
for i in range(3):
    while_6c()  # 1..6 = 0; 1,2,3,2,1,2,3,2,1 = 2; 4,2,1,2,5,1,9,2,5,2 = 3


def while_8c():  # Стандартное отклонение
    c = 0
    a = 0
    i = 0
    n = 1
    A = []
    while n != 0:
        n = int(input())
        if n != 0:
            A.append(n)
    a = sum(A)
    s = a / len(A)
    i = 0
    while i in range(len(A)):
        c = c + (A[i] - s) ** 2
        i += 1
    r = (c / (len(A) - 1)) ** 0.5
    print(r)
for i in range(3):
    while_8c()  # 1..6 = 1.87; 1,3,5,7,9,11 = 3.74; 1,2,3,2,1 = 0.83


def while_9c(a, b, N):  # Исполнитель "Водолей"
    a1 = 0
    b1 = 0

    def nod(a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b

    NOD = nod(a, b)
    if N % NOD == 0 and N <= a and N <= b:
        if a != N and b != N:
            if a < b:
                while a1 != N:
                    if a1 == 0:
                        while b1 < b:
                            b1 = b1 + a
                            print('>A')
                            print('A>B')
                        a1 = b1 - b
                        if a1 != N:
                            if b1 > b:
                                b1 = 0
                                print('B>')
                    elif a1 != 0:
                        b1 = b1 + a1
                        a1 = 0
                        print('A>B')
            elif b < a:
                while b1 != N:
                    if b1 == 0:
                        while a1 < a:
                            a1 = a1 + b
                            print('>B')
                            print('B>A')
                        b1 = a1 - a
                        if b1 != N:
                            if a1 > a:
                                a1 = 0
                                print('B>')
                    else:
                        a1 = a1 + b1
                        b1 = 0
                        print('B>A')
        elif a == N:
            print('>A')
        elif b == N:
            print('>B')
    else:
        print('Невозможно')
for i in ((3, 2, 1), (2, 3, 1), (8, 5, 1), (5, 8, 1)):
    print(*i, '->')
    while_9c(*i)
