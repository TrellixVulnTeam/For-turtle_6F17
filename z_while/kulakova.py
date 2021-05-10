def while_1c(n):  # Числа Фибоначи
    num1 = 1
    num2 = 0
    while n > 0:
        num2 += num1
        num1 = num2 - num1
        n -= 1
    print(num2)


def while_1c(n):  # Числа Фибоначи
    num1 = 1
    num2 = 0
    count = 0
    if n == 1:
        print(1)
    if n == 2:
        print(2)
    if n == 0:
        print(-1)
    if n > 2:
        for i in range(1, n - 1):
            num2 += num1
            num1 = num2 - num1
            aux = n - num2
            count += 1
        print(count if aux == 0 else -1)



def while_3c(a, b):  # Исполнитель "Раздвоитель"
    while a != b:
        if a % 2 == 1:
            a -= 1
            print("-1")
        if a / 2 > b:
            a /= 2
            print(":2")
        else:
            while a > b:
                a -= 1
                print("-1")

for i in ((10, 5), (19, 2), (17, 3), (4,3)):
    print(*i, '->')
    while_3c(*i)


def while_4c(n):  # Максимальное число идущих подряд элементов
    dely = 2
    num = 0
    sr = 1
    for i in range(1, dely):
        while n[num] != 0:
            if n[num] == n[num + 1]:
                sr += 1
            num += 1
            dely += 1
        print(sr)



def while_5c(n):  # Максимальная длинна монотонного фрагмента
    dely = 2
    num = 0
    count = 0
    count_min = 0
    for i in range(1, dely):
        while n[num] != 0:
            if n[num] < n[num + 1]:
                count += 1
            if n[num] > n[num + 1]:
                count_min += 1
            num += 1
            dely += 1
        print(max(count, count_min))


def while_6c(n):  # Количество локальных максимумов
    dely = 2
    num = 1
    count = 0
    for i in range(1, dely):
        while n[num] != 0:
            if n[num - 1] < n[num] and n[num] > n[num + 1]:
                count += 1
            num += 1
            dely += 1
        print(count)

def while_7c(n):  # Наименьшее растояние между двумя строгими максимумами
    dely = 2
    dely1 = 2
    num = 1
    num1 = 1
    maxa = 0
    for u in range(1, dely1):
        while n[num] != 0:
            if n[num1 - 1] < n[num1] and n[num1] > n[num1 + 1]:
                break
            else:
                num1 += 1
                dely1 += 1
    for i in range(1, dely):
        while n[num] != 0:
            if n[num - 1] < n[num] and n[num] > n[num + 1]:
                maxa = num
            num += 1
            dely += 1
        print(maxa - num1)

def while_8c(n):  # Стандартное отклонение
    sumcoren = 0
    new_len = len(n)
    s = (sum(n) / len(n))
    for i in range(0, new_len):
        coren = (n[i] - s) ** 2
        sumcoren += coren
    otvet = (sumcoren / (new_len - 1)) ** 0.5
    print(otvet)

def while_9c(a, b, n):  # Исполнитель "Водолей"
    b1 = 0  # доп значение в
    a1 = 0  # доп значение а
    if (n > a and n > b) or (a == b and n < a) or (a == b and n < b) or (a % 2 == 0 and b % 2 == 0 and n % 2 == 1):
        print("невозможно")
    if (a == b == n):
        print(">А")
    if a > b and n < b:
        while b1 != n:
            if b1 == 0:
                b1 += b
                print(">B")
            a1 += b1
            print("B>A")
            b1 -= b1  # опустошили б как следствие выше
            if a1 <= a:
                b1 += b
                print(">B")
                a1 += b1
                print("B>A")
                b1 -= b1  # опустошили б как следствие выше
            if a1 > a:
                b1 = a1 - a  # остаток воды не вмещаемой
                a1 -= a1  # a
                print("A>")
    if a > b and b < n < a:
        while a1 != n:
            if b1 == 0:
                b1 += b
                print(">B")
            a1 += b1
            print("B>A")
            b1 -= b1  # опустошили б как следствие выше
            if a1 <= a:
                b1 += b
                print(">B")
                a1 += b1
                print("B>A")
                b1 -= b1  # опустошили б как следствие выше
            if a1 > a:
                b1 = a1 - a  # остаток воды не вмещаемой
                a1 -= a1  # a
                print("A>")

    if b > a and a < n < b:
        while b1 != n:
            if a1 == 0:
                a1 += a
                print(">A")
            b1 += a1
            print("A>B")
            a1 -= a1  # опустошили б как следствие выше
            if b1 <= b:
                a1 += a
                print(">A")
            b1 += a1
            if b1 > b:
                a1 == 0
                a1 = b1 - b  # остаток воды не вмещаемой
                b1 -= a1
                print("A>B")
    if b > a and n < a:
        while a1 != n:
            if a1 == 0:
                a1 += a
                print(">A")
            b1 += a1
            print("A>B")
            a1 -= a1  # опустошили б как следствие выше
            if b1 <= b:
                a1 += a
                print(">A")
            b1 += a1
            if b1 > b:
                a1 == 0
                a1 = b1 - b  # остаток воды не вмещаемой
                b1 -= a1
                print("A>B")

for i in ((3, 2, 1), (2, 3, 1), (8, 5, 1), (5, 8, 1)):
    print(*i, '->')
    while_9c(*i)