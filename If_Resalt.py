import random
import math
from z_ifs import _begaev1 as temp1
from z_ifs import _begaev2 as temp2


def r_number(minis=-10, maxis=10):
    return random.randrange(minis, maxis)


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


def if_r16(a, b, c):
    if a < b < c:
        k = 2
    else:
        k = -1
    a *= k
    b *= k
    c *= k

    return a, b, c


def if_r17(a, b, c):
    if (a < b < c) or (a > b > c):
        k = 2
    else:
        k = -1
    a *= k
    b *= k
    c *= k

    return a, b, c


def if_r18(a, b, c):
    if a == b:
        return 3
    elif a == c:
        return 2
    else:
        return 1


def if_r19(a, b, c, d):
    if a == b:
        if a == d:
            return 3
        else:
            return 4
    else:
        if a == c:
            return 2
        else:
            return 1


def if_r20(a, b, c):
    ab = abs(a - b)
    ac = abs(a - c)
    if ab < ac:
        return b, ab
    elif ab > ac:
        return c, ac
    else:
        return b, c, ab


def if_r21(x, y):
    if x == 0 and y == 0:
        return 0
    elif y == 0:
        return 1
    elif x == 0:
        return 2
    else:
        return 3


def if_r22(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


def if_r23(m):
    min_x = min(m[0], m[2], m[4])
    min_y = min(m[1], m[3], m[5])
    max_x = max(m[0], m[2], m[4])
    max_y = max(m[1], m[3], m[5])
    aux = ((m[0], m[1]), (m[2], m[3]), (m[4], m[5]))
    ll = ((min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y))
    for i in ll:
        if i not in aux:
            return i


def if_r24(x):
    if x > 0:
        y = 2 * math.sin(x)
    else:
        y = 6 - x
    return y


def if_r25(x):
    if x < -2 or x > 2:
        y = 2 * x
    else:
        y = -3 * x
    return y


def if_r26(x):
    if x <= 0:
        y = -x
    elif x < 2:
        y = x * x
    else:
        y = 4
    return y


def if_r27(x):
    x_floor = math.floor(x)
    if x < 0:
        y = 0
    elif x_floor % 2 == 0:
        y = 1
    else:
        y = -1
    return y


def if_r28(i):
    s = 365
    if (i % 4 == 0) and not (i % 100 == 0 and i % 400 != 0):
        s = 366
    return s


def if_r29(i):
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
    return s


def if_r30(i):
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
    return s


def test():
    flag = True
    for i in range(10):
        a = r_number()
        if if_r1(a) != temp1.if1(a):
            flag = False
            if 1 in printing:
                print(a)
    print("Test 1 - Ok" if flag else "Test 1 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        if if_r2(a) != temp1.if2(a):
            flag = False
            if 2 in printing:
                print(a)
    print("Test 2 - Ok" if flag else "Test 2 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        if if_r3(a) != temp1.if3(a):
            flag = False
            if 3 in printing:
                print(a)
    print("Test 3 - Ok" if flag else "Test 3 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r4(a, b, c) != temp1.if4(a, b, c):
            flag = False
            if 4 in printing:
                print(a, b, c)
    print("Test 4 - Ok" if flag else "Test 4 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r5(a, b, c) != temp1.if5(a, b, c):
            flag = False
            if 5 in printing:
                print(a, b, c)
    print("Test 5 - Ok" if flag else "Test 5 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r6(a, b) != temp1.if6(a, b):
            flag = False
            if 6 in printing:
                print(a, b)
    print("Test 6 - Ok" if flag else "Test 6 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r7(a, b) != temp1.if7(a, b):
            flag = False
            if 7 in printing:
                print(a, b)
    print("Test 7 - Ok" if flag else "Test 7 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r8(a, b) != temp1.if8(a, b):
            flag = False
            if 8 in printing:
                print(a, b)
    print("Test 8 - Ok" if flag else "Test 8 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r9(a, b) != temp1.if9(a, b):
            flag = False
            if 9 in printing:
                print(a, b)
    print("Test 9 - Ok" if flag else "Test 9 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r10(a, b) != temp1.if10(a, b):
            flag = False
            if 10 in printing:
                print(a, b)
    print("Test 10 - Ok" if flag else "Test 10 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r11(a, b) != temp1.if11(a, b):
            flag = False
            if 11 in printing:
                print(a, b)
    print("Test 11 - Ok" if flag else "Test 11 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r12(a, b, c) != temp1.if12(a, b, c):
            flag = False
            if 12 in printing:
                print(a, b, c)
    print("Test 12 - Ok" if flag else "Test 12 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r13(a, b, c) != temp1.if13(a, b, c):
            flag = False
            if 13 in printing:
                print(a, b, c)
    print("Test 13 - Ok" if flag else "Test 13 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r14(a, b, c) != temp1.if14(a, b, c):
            flag = False
            if 14 in printing:
                print(a, b, c)
    print("Test 14 - Ok" if flag else "Test 14 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r15(a, b, c) != temp1.if15(a, b, c):
            flag = False
            if 15 in printing:
                print(a, b, c)
    print("Test 15 - Ok" if flag else "Test 15 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r16(a, b, c) != temp2.if16(a, b, c):
            flag = False
            if 16 in printing:
                print(a, b, c)
    print("Test 16 - Ok" if flag else "Test 16 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r17(a, b, c) != temp2.if17(a, b, c):
            flag = False
            if 17 in printing:
                print(a, b, c)
    print("Test 17 - Ok" if flag else "Test 17 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if a == b:
            a += 1
        x = random.randrange(1, 4)
        if x == 1:
            aux = (a, a, b)
        elif x == 2:
            aux = (a, b, a)
        else:
            aux = (b, a, a)
        if if_r18(*aux) != temp2.if18(*aux):
            flag = False
            if 18 in printing:
                print(*aux)
    print("Test 18 - Ok" if flag else "Test 18 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if a == b:
            a += 1
        x = random.randrange(1, 4)
        if x == 1:
            aux = (a, a, a, b)
        elif x == 2:
            aux = (a, a, b, a)
        elif x == 3:
            aux = (a, b, a, a)
        else:
            aux = (b, a, a, a)
        if if_r19(*aux) != temp2.if19(*aux):
            flag = False
            if 19 in printing:
                print(*aux)
    print("Test 19 - Ok" if flag else "Test 19 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        c = r_number()
        if if_r20(a, b, c) != temp2.if20(a, b, c):
            flag = False
            if 20 in printing:
                print(a, b, c)
    print("Test 20 - Ok" if flag else "Test 20 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if if_r21(a, b) != temp2.if21(a, b):
            flag = False
            if 21 in printing:
                print(a, b)
    print("Test 21 - Ok" if flag else "Test 21 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        b = r_number()
        if a == 0:
            a += 1
        if b == 0:
            b += 1
        if if_r22(a, b) != temp2.if22(a, b):
            flag = False
            if 22 in printing:
                print(a, b)
    print("Test 22 - Ok" if flag else "Test 22 - Fail")

    flag = True
    for i in range(200):
        temp = random.sample(range(-10, 10), 4)
        aux = (temp[0], temp[1], temp[0], temp[3], temp[2], temp[1])
        if if_r23(aux) != temp2.if23(*aux):
            flag = False
            if 23 in printing:
                print(aux)
    print("Test 23 - Ok" if flag else "Test 23 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        if if_r24(a) != temp2.if24(a):
            flag = False
            if 24 in printing:
                print(a)
    print("Test 24 - Ok" if flag else "Test 24 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        if if_r25(a) != temp2.if25(a):
            flag = False
            if 25 in printing:
                print(a)
    print("Test 25 - Ok" if flag else "Test 25 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        if if_r26(a) != temp2.if26(a):
            flag = False
            if 26 in printing:
                print(a)
    print("Test 26 - Ok" if flag else "Test 26 - Fail")

    flag = True
    for i in range(200):
        a = r_number()
        if if_r27(a) != temp2.if27(a):
            flag = False
            if 27 in printing:
                print(a)
    print("Test 27 - Ok" if flag else "Test 27 - Fail")

    flag = True
    for i in range(1000):
        a = r_number(0, 3000)
        if if_r28(a) != temp2.if28(a):
            flag = False
            if 28 in printing:
                print(a)
    print("Test 28 - Ok" if flag else "Test 28 - Fail")

    flag = True
    for i in range(200):
        a = r_number(-100, 100)
        if if_r29(a) != temp2.if29(a):
            flag = False
            if 29 in printing:
                print(a, if_r29(a),temp2.if29(a))
    print("Test 29 - Ok" if flag else "Test 29 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 1000)
        if if_r30(a) != temp2.if30(a):
            flag = False
            if 30 in printing:
                print(a)
    print("Test 30 - Ok" if flag else "Test 30 - Fail")

printing = (0, 20, 21)

test()
