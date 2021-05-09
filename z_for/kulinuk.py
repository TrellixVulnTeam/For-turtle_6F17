import math


def for_1a(a, b):
    for a in range(b):
        print(a+1)

def for_3a(n):
    n1=0
    for i in range(n+1):
        n=i**3
        n1=n1+n
    print (n1)


def for_1b(n):
    a = 0
    for i in range(n):
        i = i + 1
        a = a + ((i) - 1) * (i)
        if i == 1:
            pass
        elif i == 2:
            print(f'{i - 1}*{i}', end='')
        else:
            print(f'+{i - 1}*{i}', end='')

    print(' =', a)


def for_2b(a, b):
    for i in range(a, b):
        while i % 2 != 0:
            i = i + 1
            print(i)


def for_6b(n):
    for i in range(10, 100):
        if ((i // 10) * (i % 10)) * 2 == i:
            print(i)
        else:
            pass


def for_7b(n):
    for i in range(100, 1000):
        jo = i // 100
        ho = i % 10
        ko = (i % 100) // 10
        if jo + ko + ho == n:
            print(i)


def for_1c(n):
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            print(k, sep='', end='')
        print()
for i in range (10):
    for_1c(i)

def for_2c(a, b, c, d, e):
    c = 0
    for i in range(0, 1000):
        if i - e == 0:
            pass
        else:
            k = (a * (i ** 3) + b * (i ** 2) + (c * i) + d) / (i - e)
            if k == 0:
                c = c + 1
    return (c)
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


def for_3c(a, b):
    for i in range(a, b):
        i1 = f'{i}'
        if i1[0] == i1[3] and i1[1] == i1[2]:
            print(i)
for_3c(1000, 9999)


def for_4c(a, b):
    for i in range(a, b):
        i1 = f'{i}'
        if i1[0] == i1[1] == i1[2] != i1[3] or i1[1] == i1[2] == i1[3] != i1[0] or i1[0] == i1[2] == i1[3] != i1[1]:
            print(i)
for_4c(1000, 9999)


def for_5c(a, b, c, d):
    for i in range(a, b + 1):
        while i % d == c:
            print(i)
            i = i + 1


def for_6c():
    n = int(input())
    k = n
    k1 = 0
    for i in range(1, n):
        k = k + i
        k1 = k1 + int(input())
    print(k - k1)



def for_7c(k):
    count = 1
    for i in range(1, k + 1):
        print(count, end='')
        if i == count * (count + 1) // 2:
            count = count + 1
for i in range(20):
    print()
    for_7c(i)


def for_8c(n):
    j = 1
    k = 0
    for i in range(n):
        j = j * (i + 1)
        k = k + j
    return (k)
for i in range(1,20):
    if not for_8c(i) == sum(math.factorial(j) for j in range(1, i+1)):
        print('\n Fail!', i, for_8c(i), sum(math.factorial(j) for j in range(i)), end='')