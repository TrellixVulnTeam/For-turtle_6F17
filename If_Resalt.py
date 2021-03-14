import random
import math
import _kulinuk as temp


def r_number(min = -10, max = 10):
    return random.randrange(min, max)

def if_r1(a):
    if a > 0:
        a -= 8
    return a
def if_r2(a):

    if a > 0:
        a -= 8
    else:
        a += 6
    return a
def if_r3(a):
    if a > 0:
        a -= 8
    elif a < 0:
        a += 6
    else:
        a = 10
    return a
def if_r4(a, b, c):
    x = 0
    if a > 0:
        x += 1
    if b > 0:
        x += 1
    if c > 0:
        x += 1
    return x
def if_r5(a, b, c):
    x = 0
    if a > 0:
        x += 1
    if b > 0:
        x += 1
    if c > 0:
        x += 1
    y = 0
    if a < 0:
        y += 1
    if b < 0:
        y += 1
    if c < 0:
        y += 1
    return x, y
def if_r6(a, b):
    if a > b:
        _max = a
    else:
        _max = b
    return _max
def if_r7(a, b):
    if a < b:
        _min = 1
    else:
        _min = 2
    return _min
def if_r8(a, b):
    if a > b:
        return a, b
    else:
        return b, a
def if_r9(a, b):
    if a > b:
        a, b = b, a
    return a, b
def if_r10(a, b):
    if a != b:
        a = b = a + b
    else:
        a = b = 0
    return a, b
def if_r11(a, b):
    if a != b:
        a = b = max(a, b)
    else:
        a = b = 0
    return a, b
def if_r12(a, b, c):
    if a < b:
        mn = a
    else:
        mn = b
    if mn > c:
        mn = c
    return mn
def if_r13(a, b, c):
    m = False
    if (a <= b <= c) or (c <= b <= a):
        m = b
    elif (b <= a <= c) or (c <= a <= b):
        m = a
    elif (a <= c <= b) or (b <= c <= a):
        m = c
    return m
def if_r14(a, b, c):
    if a < b:
        mn = a
        mx = b
    else:
        mn = b
        mx = a
    if mx < c:
        mx = c
    if mn > c:
        mn = c

    return mn, mx
def if_r15(a, b, c):
    m = False
    if (c <= a <= b) or (c <= b <= a):
        m = a + b
    elif (b <= a <= c) or (b <= c <= a):
        m = a + c
    elif (a <= c <= b) or (a <= b <= c):
        m = b + c

    return m

def if_r16():
    A = random.randrange(-30, 30)
    B = random.randrange(-30, 30)
    C = random.randrange(-30, 30)
    print("Число A:", A)
    print("Число B:", B)
    print("Число C:", C)
    if (A < B and B < C):
        k = 2
    else:
        k = -1
    A *= k
    B *= k
    C *= k

    print()
    print("Число A:", A)
    print("Число B:", B)
    print("Число C:", C)


def if_r17():
    A = random.randrange(-30, 30)
    B = random.randrange(-30, 30)
    C = random.randrange(-30, 30)
    print("Число A:", A)
    print("Число B:", B)
    print("Число C:", C)
    if (A < B and B < C) or (A > B and B > C):
        k = 2
    else:
        k = -1
    A *= k
    B *= k
    C *= k

    print()
    print("Число A:", A)
    print("Число B:", B)
    print("Число C:", C)


def if_r18():
    def RandNum():
        l = []
        x1, x2 = random.sample(range(-10, 10), 2)
        N = random.randrange(1, 4)
        if N == 1:
            l.append(x1)
            l.append(x1)
            l.append(x2)
        elif N == 2:
            l.append(x1)
            l.append(x2)
            l.append(x2)
        else:
            l.append(x2)
            l.append(x1)
            l.append(x2)
        return l

    A, B, C = RandNum()
    print("Число A:", A)
    print("Число B:", B)
    print("Число C:", C)
    if A == B:
        print("C")
    elif A == C:
        print("B")
    else:
        print("A")


def if_r19():
    def RandNum():
        l = []
        x1, x2 = random.sample(range(-10, 10), 2)
        N = random.randrange(1, 5)
        if N == 1:
            l.append(x2)
            l.append(x1)
            l.append(x1)
            l.append(x1)
        elif N == 2:
            l.append(x1)
            l.append(x2)
            l.append(x1)
            l.append(x1)
        elif N == 3:
            l.append(x1)
            l.append(x1)
            l.append(x2)
            l.append(x1)
        else:
            l.append(x1)
            l.append(x1)
            l.append(x1)
            l.append(x2)
        return l

    A, B, C, D = RandNum()
    print("Число A:", A)
    print("Число B:", B)
    print("Число C:", C)
    print("Число D:", D)
    if A == B:
        if A == D:
            print("C")
        else:
            print("D")
    else:
        if A == C:
            print("B")
        else:
            print("A")


def if_r120():
    A, B, C = random.sample(range(-10, 10), 3)
    print("Число A:", A)
    print("Число B:", B)
    print("Число C:", C)
    AB = abs(A - B)
    AC = abs(A - C)
    print("Расстояние от A до B:", AB)
    print("Расстояние от A до C:", AC)
    if AB < AC:
        print("В ближе к A")
    elif AB > AC:
        print("C ближе к A")
    else:
        print("B и C равноудалены от A")


def if_r21():
    for i in range(0, 5):
        x, y = [random.randrange(-3, 4) for i in range(0, 2)]
        print("\nТочка (x,y): ({0},{1})".format(x, y))
        if x == 0 and y == 0:
            print("0. Совпадает с началом координат")
        elif y == 0:
            print("1. Лежит на оси OX")
        elif x == 0:
            print("2. Лежит на оси OY")
        else:
            print("3. Не лежит на координатных осях")


def if_r22():
    lst = [i for i in list(range(-10, 11)) if i != 0]
    for i in range(0, 5):
        x = random.choice(lst)
        y = random.choice(lst)
        print("\nТочка (x, y): ({0},{1})".format(x, y))
        print("Координатная четверть: ", end="")
        if x > 0 and y > 0:
            print("I")
        elif x < 0 and y > 0:
            print("II")
        elif x < 0 and y < 0:
            print("III")
        else:
            print("IV")


def if_r23():
    x1, x2 = sorted(random.sample(range(-10, 11), 2))
    y2, y1 = sorted(random.sample(range(-10, 11), 2))
    L = [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]
    print(L)
    random.shuffle(L)
    print(L)
    M = L[:3]
    print(M)
    print("Вершина 1: ({0},{1})".format(M[0][0], M[0][1]))
    print("Вершина 2: ({0},{1})".format(M[1][0], M[1][1]))
    print("Вершина 3: ({0},{1})".format(M[2][0], M[2][1]))
    print()
    min_x = min(M[0][0], M[1][0], M[2][0])
    min_y = min(M[0][1], M[1][1], M[2][1])
    max_x = max(M[0][0], M[1][0], M[2][0])
    max_y = max(M[0][1], M[1][1], M[2][1])
    L = [[min_x, min_y], [min_x, max_y], [max_x, min_y], [max_x, max_y]]
    for i in L:
        if i not in M:
            print("Вершина 4: ({0},{1})".format(i[0], i[1]))


def if_r24():
    for i in range(-5, 6):
        h = i / 2
        x = math.pi * h
        if x > 0:
            y = 2 * math.sin(x)
        else:
            y = 6 - x
        print("h = {0} : x = {1:.4f} : f(x) = {2:.4f}".format(h, x, y))


def if_r25():
    for x in range(-4, 5):
        if x < -2 or x > 2:
            y = 2 * x
        else:
            y = -3 * x
        print("x = {0} : f(x) = {1}".format(x, y))


def if_r26():
    for i in range(-2, 7):
        x = i / 2
        if x <= 0:
            y = -x
        elif x < 2:
            y = x * x
        else:
            y = 4
        print("x = {0} : f(x) = {1}".format(x, y))


def if_r27():
    x = -1
    while x < 11:
        x_floor = math.floor(x)
        if x < 0:
            y = 0
        elif x_floor % 2 == 0:
            y = 1
        else:
            y = -1
        print("x = {0} : f(x) = {1}".format(x, y))
        x += .5


def if_r28():
    L = [2016, 300, 1300, 1900, 1200, 2000]
    for i in L:
        s = "не високосный"
        if (i % 4 == 0) and not (i % 100 == 0 and i % 400 != 0):
            s = "високосный"
        print(i, " : ", s)
        if (i % 4 == 0) and (i % 100 != 0 or i % 400 == 0):
            s = "високосный"
        print(i, " : ", s)


def if_r29():
    for i in range(-4, 5):
        if i == 0:
            s = "нулевое "
        elif i > 0:
            s = "положительное "
        else:
            s = "отрицательное "
        if i != 0:
            if i % 2 == 0:
                s += "четное "
            else:
                s += "нечетное "
        s += "число"
        print(i, " : ", s)


def if_r30():
    L = [1, 21, 80, 99, 100, 101, 800, 901, 999]
    for i in L:
        if i % 2 == 0:
            s = "четное "
        else:
            s = "нечетное "
        i_str = str(i)
        n = len(i_str)
        if n == 1:
            s += "однозначное "
        elif n == 2:
            s += "двузначное "
        elif n == 3:
            s += "трехзначное "

        s += "число"
        print(i, " : ", s)

def test():
    flag = True
    for i in range(10):
        a = r_number()
        if if_r1(a) != temp.if1(a):
            flag = False
    print("Test 1 - Ok" if flag == True else "Test 1 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        if if_r2(a) != temp.if2(a):
            flag = False
    print("Test 2 - Ok" if flag == True else "Test 2 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        if if_r3(a) != temp.if3(a):
            flag = False
    print("Test 3 - Ok" if flag == True else "Test 3 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r4(a, b, c) != temp.if4(a, b, c):
            flag = False
    print("Test 4 - Ok" if flag == True else "Test 4 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r5(a, b, c) != temp.if5(a, b, c):
            flag = False
    print("Test 5 - Ok" if flag == True else "Test 5 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r6(a, b) != temp.if6(a, b):
            flag = False
    print("Test 6 - Ok" if flag == True else "Test 6 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r7(a, b) != temp.if7(a, b):
            flag = False
    print("Test 7 - Ok" if flag == True else "Test 7 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r8(a, b) != temp.if8(a, b):
            flag = False
    print("Test 8 - Ok" if flag == True else "Test 8 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r9(a, b) != temp.if9(a, b):
            flag = False
    print("Test 9 - Ok" if flag == True else "Test 9 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r10(a, b) != temp.if10(a, b):
            flag = False
    print("Test 10 - Ok" if flag == True else "Test 10 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r11(a, b) != temp.if11(a, b):
            flag = False
    print("Test 11 - Ok" if flag == True else "Test 11 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r12(a, b, c) != temp.if12(a, b, c):
            flag = False
    print("Test 12 - Ok" if flag == True else "Test 12 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r13(a, b, c) != temp.if13(a, b, c):
            flag = False
    print("Test 13 - Ok" if flag == True else "Test 13 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r14(a, b, c) != temp.if14(a, b, c):
            flag = False
    print("Test 14 - Ok" if flag == True else "Test 14 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r15(a, b, c) != temp.if15(a, b, c):
            flag = False
    print("Test 15 - Ok" if flag == True else "Test 15 - Fail")


def fined():
    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        print((a, b) if if_r9(a, b) != temp.if9(a, b) else "Ok")
        if if_r9(a, b) != temp.if9(a, b):
            flag = False
    print("Test 13- Ok" if flag == True else "Test 13 - Fail")

#test()
fined()
