def for_3a(n): # Сумма кубов
    c=0
    for i in range(1,n+1):
        c=c+(i**3)
    print(c)


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


def for_2b(a, b): # Чётные числа
    for i in range(a,b,2):
        print((i%2)+i, end=' ')


def for_6b(n): # Замечательные числа
    for i in range(10, 100):
        n2 = i % 10
        n1 = i // 10
        c=2 * n1 * n2
        if c == i:
            print(i)

def for_7b(n): # Замечательные числа 2
    for i in range(100,1000):
        helper=i%100
        n2=helper%10
        n1=helper//10
        n3=i//100
        if (n2+n1+n3)==n:
            print(i)


def for_1c(n): # Лесенка
    a=[]
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()


def for_2c(a, b, c, d, e): # Диофантово уравнение
    c=0
    for i in range(0,1000):
        if i-e>0:
            if ((a * (i) ** 3 + b * (i) ** 2 + d)/(i-e))==0:
                c+=1
    print(c)


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


def for_5c(a, b, c, d): # Остатки
    a = (a-c+d-1)//d*d+c
    for i in range(a,b+1,d):
        print(i, end=' ')


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


def for_8c(n): # Сумма факториалов
    r=1
    a=0
    for i in range(1,n+1):
        r=r*i
        a=a+r
    print(a)