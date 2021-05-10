import math

def for_1a(a, b):
    for i in range(a, b + 1):
        print(i, end=" ")


def for_2a(n):
    for i in range(10 ** n, 10 ** (n - 1), -1):
        if i % 2:
            print(i)


def for_3a(n):  # Сумма кубов
    s = 0
    for i in range(n + 1):
        s += i ** 3
    print(s)


def for_5a(n):  # Пингвины
    print("    _~_     " * n)
    print("   (o o)    " * n)
    print("  /  V  \   " * n)
    print(" /(  _  )\  " * n)
    print("   ^^ ^^    " * n)
for_5a(10)

def for_6a(n):  # Флаги
    print('+___ ' * n)
    for i in range(n):
        print('|', i + 1, ' /', sep='', end=' ')
    print()  # p
    print('|__\\ ' * n)
    print('|    ' * n)
for_6a(10)


def for_1b(n):  # Сумма произведений соседних чисел
    s = 0
    for i in range(1, n):
        s += i*(i+1)
    for j in range(1, n-1):
        print(f'{j}*{j+1}+', end='')
    print(f'{n-1}*{n}=', end='')
    print(s)



def for_2b(a, b):  # Чётные числа
    for i in range(a, b+1, 2):
        print((i % 2)+i)


def for_3b(n):  # Сумма N чисел
    s = 0
    for i in range(1, n+1):
        n = int(input())
        s += n
    print(s)


def for_4b(n):  # Сумма десяти чисел
    s = 0
    for i in range(10):
        n = int(input())
        s += n
    print(s)



def for_5b(n):  # Количество нулей
    k = 0
    for i in range(n):
        n = int(input())
        if n == 0:
            k += 1
    print(k)


def for_6b(n):  # Замечательные числа
    for i in range(10, 100):
        if (i % 10)*(i//10)*2 == i:
            print(i)


def for_7b(n):  # Замечательные числа 2
    for i in range(100, 1000):
        if n == i//100+i % 10+i % 100//10:
            print(i)

def for_1c(n):  # Лесенка
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()


def for_2c(a, b, c, d, e):  # Диофантово уравнение
    x = 0
    for i in range(1001):
        if (i-e) != 0:
            if (a*i**3+b*i**2+c*i+d)/(i-e) == 0:
                x += 1
    return ( x)
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
    for i in range(a, b+1):
        c1 = (i//100)
        c2 = (c1//10)
        c3 = (c1 % 10)
        if str(i % 100) == str(c3)+str(c2):
            print(i)
for_3c(1000, 9999)

def for_4c(a, b):  # Замечательные числа 2
    for i in range(a, b+1):
        c1 = i//1000
        c2 = i//100 % 10
        c3 = i % 100//10
        c4 = i % 10
        if c1 == c2 == c3 != c4:
            print(i)
        if c4 == c2 == c3 != c1:
            print(i)
        if c4 == c1 == c3 != c2:
            print(i)
        if c4 == c2 == c3 != c3:
            print(i)
for_4c(1000, 9999)

def for_5c(a, b, c, d):  # Остатки
    pass


def for_6c(n):  # Потерянная карточка
    n = int(input())
    s = 0
    s2 = 0
    for i in range(n-1):
        a = int(input())
        s += a
    for i in range(n+1):
        s2 += i
    print(s2-s, "card")


def for_7c(k):  # Треугольная последовательность
    for i in range(1, k+1):
        print(str(i)*i, end='')
for i in range(20):
    print()
    for_7c(i)

def for_8c(n):  # Сумма факториалов
    f1 = 1
    f2 = 0
    for i in range(1, n+1):
        f1 *= i
        f2 += f1
    return (f2)
for i in range(1,20):
    if not for_8c(i) == sum(math.factorial(j) for j in range(1, i+1)):
        print('\n Fail!', i, for_8c(i), sum(math.factorial(j) for j in range(i)), end='')