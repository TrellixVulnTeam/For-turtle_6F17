import math
def for_3a(n): # Сумма кубов
    c=0
    for i in range(1,n+1):
        c=c+(i**3)
    return c
for i in range (10):
    if sum(j**3 for j in range(1, i+1)) == for_3a(i):
        print('Ok')
    else:
        print(sum(j**3 for j in range(1, i+1)), for_3a(i))


def for_6a(n): # Флаги
    for i in range(n):
        print("+___", end=" ")
    print()
    for i in range(1, n + 1):
        print(f'|{i} /', end=" ")
    print()
    for i in range(n):
        print("|__\\", end=" ")
    print()
    for i in range(n):
        print("|   ", end=" ")
    print()
for i in range (10):
    for_6a(i)


def for_1b(n): # Сумма произведений соседних чисел
    y=2
    c=1
    a=0
    print(f'1*2',end='')
    for i in range(2,n+1):
        a=a+(c*i)
        c+=1
    for t in range(2,n):
        if n>2:
            r=t+1
            print(f'+{y}*{r}', end='')
            y+=1
    if n<2:
        print('Ошибка')
    else:
        print('=', a, sep='')
for i in range (10):
    for_1b(i)


def for_2b(a, b): # Чётные числа
    for i in range(a,b,2):
        print((i%2)+i, end=' ')
a = 1
for b in range (1, 20, 2):
    for_2b(a, b)
    print()


def for_6b(): # Замечательные числа
    for i in range(10, 100):
        n2 = i % 10
        n1 = i // 10
        c=2 * n1 * n2
        if c == i:
            print(i)
for_6b() # Ответ 36


def for_7b(n): # Замечательные числа 2
    for i in range(100,1000):
        helper=i%100
        n2=helper%10
        n1=helper//10
        n3=i//100
        if (n2+n1+n3)==n:
            print(i)
for i in (0, 2, 3, 26, 27):
    print(i)
    for_7b(i)


def for_1c(n): # Лесенка
    a=[]
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
for i in range (10):
    for_1c(i)


def for_2c(a, b, c, d, e): # Диофантово уравнение
    c = 0
    for i in range(0,1000):
        if i-e>0:
            if ((a * (i) ** 3 + b * (i) ** 2 + d)/(i-e))==0:
                c += 1
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


def for_3c(a, b): # Замечательные числа
    for i in range(a,b):
        helper1=i%1000
        helper2=helper1%100
        x1=i//1000
        x2=helper1//100
        x3=helper2//10
        x4=i%10
        if x1==x4 and x2==x3:
            print(i)
for_3c(1000, 9999)


def for_4c(a, b): # Замечательные числа 2
    for i in range(a, b):
        helper1 = i % 1000
        helper2 = helper1 % 100
        x1 = i // 1000
        x2 = helper1 // 100
        x3 = helper2 // 10
        x4 = i % 10
        if x1==x2==x3 or x2==x3==x4 or x1==x3==x4 or x4==x2==x1:
            print(i)
for_4c(1000, 9999)


def for_5c(a, b, c, d): # Остатки
    a = (a-c+d-1)//d*d+c
    for i in range(a,b+1,d):
        print(i, end=' ')
for a in ((1, 100, 3, 33),(1, 100, 0, 25),(1, 100, 6, 7),(10, 100, 4, 50),(1, 100, 1, 2)):
    print()
    print(*a, end = "->")
    for_5c(*a)


def for_6c(n): # Потерянная карточка
    a=0
    c=0
    for j in range(1,n+1):
        a=a+j
    for i in range(1,n):
        x1 = (int(input()))
        c=c+x1
    print(a-c)


def for_7c(k): # Треугольная последовательность
    a = 1
    for i in range(1, k + 1):
        print(a, end=' ')
        if i == a * (a + 1) // 2:
            a += 1
for i in range(20):
    print()
    for_7c(i)

def for_8c(n): # Сумма факториалов
    r=1
    a=0
    for i in range(1,n+1):
        r=r*i
        a=a+r
    return (a)
for i in range(1,20):
    if not for_8c(i) == sum(math.factorial(j) for j in range(1, i+1)):
        print('\n Fail!', i, for_8c(i), sum(math.factorial(j) for j in range(i)), end='')