def while_1a(n): # Список квадратов
    k=1
    while k<n:
        print(k**2,end=' ')
        k+=1


def while_1b():  # Среднее значение
    q = -1
    summ = 0
    w = 7
    while w != 0:
        w = int(input())
        summ += w
        q += 1
    print(summ / q)


def while_2b():  # Маесимум поседовательности
    MAX = 0
    w = 7
    while w != 0:
        w = int(input())
        if MAX < w:
            MAX = w
    print(MAX)


def while_1c():  # Числа Фибоначи
    n = int(input())
    k = 1
    r = 1  # предыдущие k
    rr = 0  # предыдущие r
    while n > 1:
        k = r + rr
        n -= 1
        if rr <= r:
            rr = k
        else:
            r = k
    print(k)


def while_2c():  # Номер числа Фибоначи
    q = int(input())
    n = 1
    k = 1
    r = 1  # предыдущие k
    rr = 0  # предыдущие r
    b = 1
    while n != 0:
        k = r + rr
        if k == q:
            b += 1
            n = 0
        else:
            b += 1
            if rr <= r:
                rr = k
            else:
                r = k

    print(b)


def while_3c(a, b):  # Исполнитель "Раздвоитель"
    while a != b:
        if (a // 2 >= b) and (a % 2 == 0):
            print(':2')
            a //= 2
        else:
            print('-1')
            a -= 1
for i in ((10, 5), (19, 2), (17, 3), (4,3)):
    print(*i, '->')
    while_3c(*i)

def while_4c():  # Максимальное число идущих подряд элементов
    q = -1
    w = 0
    mw = 0
    n = int(input())
    while n != 0:
        if q == n:
            w += 1
        else:
            q = n
            mw = max(mw, w)
            w = 1
        n = int(input())
    mw = max(mw, w)
    print(mw)
    w = 0
    mw = 0
    n = int(input())
    while n != 0:
        if q == n:
            w += 1
        else:
            q = n
            mw = max(mw, w)
            w = 1
        n = int(input())
    mw = max(mw, w)
    print(mw)


def while_5c():  # Максимальная длинна монотонного фрагмента
    n = int(input())
    s = 0
    ss = 0
    while n != 0:
        k = n
        n = int(input())
        if (k - n) > 0:
            r = 1
        elif (k - n) < 0:
            r = -1
        else:
            r = 0
        if r < 0:
            ss -= 1
            if abs(ss) > abs(s):
                s = ss
        if r > 0:
            ss += 1
            if abs(ss) > abs(s):
                s = ss
        if r == 0:
            ss = 0
    print(abs(s) + 1)
for i in range(3):  # 1,2,3,4,5,6 = 6; 3,2,1,2 = 3; 3,2,1,2,3,4,5,6 = 6
    while_5c()