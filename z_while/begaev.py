def while_7a(): # Сумма последовательности
    a=int(input())
    b=a
    while b!=0:
        b=int(input())
        a+=b
    print(a)

def while_5b(): # Второй максимум - 2
    a=int(input())
    b=a
    while b!=0:
        b=int(input())
        if a<b:
            c=a
            a=b
        elif a==b:
            c=a
    print(c)


def while_6b(): # Количество элементов равных максимуму
    a=int(input())
    b=a
    k=0
    while b!=0:
        b=int(input())
        if a<b:
            a=b
            k=1
        elif a==b:
            k+=1
    print(k)


def while_7b(): # Сумма последовательности - 2
    k=0
    a=1
    b=0
    while b!=2 :
        a=int(input())
        if a==0:
            b+=1
        else:
            b=0
        k+=a
    print(k)


def while_1c(n):  # Числа Фибоначи

    k = 0
    a = 0
    b = 0
    c = 1
    while k != n:
        a = 0
        a += b
        a += c
        c = b
        b = a
        k += 1
    print(a)
for i in (3, 6, 10, 12):
    while_1c(i)

def while_2c( n):  # Номер числа Фибоначи
    k = 0
    a = 0
    b = 0
    c = 1
    while (a != n) and n > b:
        a = 0
        a += b
        a += c
        c = b
        b = a
        k += 1
    print(k if a == n else -1)
for i in (2, 8, 10, 55, 144):
    while_2c(i)

def while_3c(a, b):  # Исполнитель "Раздвоитель"
    while a != b:
        while a % 2 != 0:
            a -= 1
            print('-1')
        while a / 2 < b and a != b:
            a -= 1
            print('-1')
        if a / 2 < b:
            pass
        else:
            a /= 2
            print(':2')
for i in ((10, 5), (19, 2), (17, 3), (4,3)):
    print(*i, '->')
    while_3c(*i)

def while_4c():  # Максимальное число идущих подряд элементов
    a = int(input())
    k = 1
    m = 1
    b = 0
    while a != 0:
        while b == a:
            k += 1
            a = int(input())
        if k > m:

            m = k
            k = 1
        else:
            b = a
            a = int(input())
    print(m)
'''for i in range(3):  # 1,2,2,3,3,3,2,2,2,2,1 = 4; 1,2,3,2,1 = 1; 1,9,6,5,5,5,3,4 = 3
    while_4c()'''

def while_5c():  # Максимальная длинна монотонного фрагмента
    a = int(input())
    k = 1
    m = 0
    b = 0
    c = 1
    while a != 0:
        b = 0
        while a > b and a != 0:
            b = a
            a = int(input())
            if a == 0:
                pass
            else:
                if a > b:
                    k += 1
                elif a < b:
                    c += 1
            break
        if a == 0:
            pass
        else:
            a = int(input())
            if a == 0:
                pass
            else:
                b = int(input())
            while a != 0 and b != 0:
                if a > b:
                    k += 1
                elif a < b:
                    c += 1
                break
        if a > b:
            m = k
        elif a < b:
            m = c
        m = max(k, c)
        if a == 0:
            pass
        else:
            a = int(input())
        g = max(k, c, m)
    print(g)
'''for i in range(3):  # 1,2,3,4,5,6 = 6; 3,2,1,2 = 3; 3,2,1,2,3,4,5,6 = 6
    while_5c()'''

def while_6c():  # Количество локальных максимумов
    a = int(input())
    k = 0
    while a != 0:
        b = int(input())
        if b == 0:
            a = b
        if b > a:
            a = int(input())
            if b > a:
                k += 1
    print(k)
'''for i in range(3):
    while_6c()  # 1..6 = 0; 1,2,3,2,1,2,3,2,1 = 2; 4,2,1,2,5,1,9,2,5,2 = 3'''

def while_7c():  # Наименьшее растояние между двумя строгими максимумами
    a = int(input())
    c = 0
    h = 0
    m = 0
    k = 0
    while a != 0:
        b = int(input())
        if b == 0:
            a = b
        if b > a:
            a = int(input())
            c += 1
            if b > a:
                k += 1
                if k == 1:
                    pass
                elif k == 2:
                    m = c
                    c = 0
                else:
                    m = c
                    c = 0

        else:
            c += 1
    if m == 0:
        print(c)
    elif c == 0 or c == 1:
        print(m)
    else:
        print(min(c, m, ))


def while_8c():  # Стандартное отклонение
    a = int(input())
    k = 0
    s = 0
    m = 0
    mas = []
    while a != 0:
        k += 1
        s += a
        mas.append(a)
        a = int(input())
    s = s / k
    for i in mas:
        m = m + ((i - s) ** 2)
    u = (m / (k - 1)) ** 0.5
    print(u)
'''for i in range(3):
    while_8c()  # 1..6 = 1.87; 1,3,5,7,9,11 = 3.74; 1,2,3,2,1 = 0.83'''

def while_9c(k, l, n):  # Исполнитель "Водолей"
    a = min(k, l)
    b = max(k, l)
    x = 0
    y = 0
    while x != n or n != n:
        if a < n or b < n:
            print('Невозможно')
            x = n
        else:
            x += a
            print('>A')
            # print('x',x,'y',y)
        if y == 0 and (x != n or n != n):
            y += x
            x = 0
            print('A>B')
            # print('x',x,'y',y)
        elif (x + y) > b and (x != n or n != n):
            y = y + (x - n)
            x = x - (x - n)
            print('A>B')
            # print('x',x,'y',y)
        elif (x != n or n != n):
            y += x
            x = 0
            print('A>B')
            # print('x',x,'y',y)

for i in ((3, 2, 1), (2, 3, 1), (8, 5, 1), (5, 8, 1)):
    print(*i, '->')
    while_9c(*i)