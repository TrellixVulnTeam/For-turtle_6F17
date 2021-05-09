import math
def for_5a(n):  # Пингвины
    def brows(n):
        for i in range(n):
            print("  _~_   ", end="")

    def eyes(n):
        print(end="\n")
        for i in range(n):
            print(" (o o)  ", end="")

    def beak(n):
        print(end="\n")
        for i in range(n):
            print(" / v \  ", end="")

    def body(n):
        print(end="\n")
        for i in range(n):
            print("/( _ )\ ", end="")

    def claws(n):
        print(end="\n")
        for i in range(n):
            print(" ^^ ^^  ", end="")

    brows(n)
    eyes(n)
    beak(n)
    body(n)
    claws(n)


def for_6a(n):  # Флаги
    def start(n):
        for i in range(1, n + 1):
            print("+___  ", end="")

    def number(n):
        print(end="\n")
        for i in range(1, n + 1):
            print("|", i, "/ ", end="")

    def flag(n):
        print(end="\n")
        for i in range(1, n + 1):
            print("|___\ ", end="")

    def stick(n):
        print(end="\n")
        for i in range(1, n + 1):
            print("|     ", end="")

    start(n)
    number(n)
    flag(n)
    stick(n)


def for_2b(a, b):# Чётные числa
    a-=1
    n=a%2
    a=a+2-n
    for i in range(a,b+1,2):
        print(i, end=" ")


def for_3b(n): # Сумма N чисел
    sum=0
    for i in range(1,n+1):
        c=int(input("введите число"))
        sum+=c
    print(sum)


def for_4b(n): # Сумма N чисел
    sum=0
    for i in range(1,n):
        print("№",i," - ",end="")
        c=int(input("введите число "))
        sum+=c
    print(sum)



def for_1c(n):  # Лесенка
    for i in range(1, n + 1):
        for v in range(1, i + 1):
            print(v, end="")
        print()
for i in range (10):
    for_1c(i)


def for_3c(a, b):  # Замечательные числа
    a_sr1 = max(a // 100 % 10, a % 100 // 10)
    b_min = min(b // 100 % 10, b % 100 // 10)  # меньший в последнем числе

    tch1 = (a // 1000)  #
    tch2 = (b // 1000)  #

    n1 = (tch1 * 10 + a_sr1)
    n2 = (tch2 * 10 + b_min)
    n3 = (tch2 - tch1)
    cht = n2 - n1 + n3
    for t in range(1, cht):
        print(tch1 * 1000 + a_sr1 * 110 + tch1)
        a_sr1 += 1
        a_sr1 = a_sr1 % 10
        tch1 += (9 - a_sr1) % 10 // 9
for_3c(1000, 9999)

def for_5c(a, b, c, d):  # Остатки
    s = a + (d - (d - c))
    for i in range(a + s, b, d):
        print(i, end = " ")
for a in ((1, 100, 3, 33),(1, 100, 0, 25),(1, 100, 6, 7),(10, 100, 4, 50),(1, 100, 1, 2)):
    print()
    print(*a, end = "->")
    for_5c(*a)


def for_6c(n):
    ne = 0
    p = 0
    for i in range(1, n):
        num = int(input("введите карту "))
        ne += num
    for g in range(1, n + 1):
        p += g
    print(p - ne)


def for_7c(n):
    for i in range(1, n + 1):
        for n in range(0, i):
            print(i, end="", sep="")
for i in range(20):
    print()
    for_7c(i)


def for_8c(n):  # Сумма факториалов
    fact = 1
    sumfact = 0
    for i in range(1, n + 1):
        fact = fact * i
        sumfact = fact + sumfact
    return (sumfact)
for i in range(1,20):
    if not for_8c(i) == sum(math.factorial(j) for j in range(1, i+1)):
        print('\n Fail!', i, for_8c(i), sum(math.factorial(j) for j in range(i)), end='')