import math
def for_1a(a, b):
    for i in range(a, b + 1):
        print(i, end=' ')


def for_3a(n):  # Сумма кубов
    q = 0
    for i in range(1, n + 1):
        n = i ** 3
        q += n
    print(q)

def for_1b(n): # Сумма произведений соседних чисел
    w=1
    v=0
    for i in range(2,n+1):
        v+=w*i
        w+=1
    for i in range(1,n):
        print(f'{i}*{i+1}',end='')
        if i==n-1:
            print('=',v,end='')
        else:
            print('+',end='')


def for_2b(a, b): # Чётные числа
    a-=1
    n=a%2
    a=a+2-n
    for i in range(a,b+1,2):
        print(i,end=' ')


def for_6b(n): # Замечательные числа
    for i in range(10,100):
        q=i%10
        w=i//10
        if 2*q*w==i:
            print(i)

def for_1c(n): # Лесенка
    for i in range (1,n+1):
        for t in range(1,i+1):
            print(t,sep='',end='')
        print()
for i in range (10):
    for_1c(i)


def for_2c(a, b, c, d, e): # Диофантово уравнение
    a=0
    for i in range(1,1001):
        if i==e:
            a=a
        elif(a*i**3+b*i**2+c*i+d)/(i-e)==0:
            a+=1
    return (a)
def for_21c(a, b, c, d, e): # Диофантово уравнение
    count = 0
    for i in range(0,1001):
        if i !=e :
            if (a * i**3 + b * i**2 + i * c + d)/(i-e)==0:
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
    for i in range(a,b+1):
        a=(i%10)*1000
        b=10*(i%100-i%10)
        c=(i%1000-i%100)/10
        d=i//1000
        if i==a+b+c+d:
            print(i)
for_3c(1000, 9999)

def for_4c(a, b): # Замечательные числа 2
    def qqq(i):
        x=i%10
        y=(i%100-i%10)//10
        c=(i%1000-i%100)//100
        d=i//1000
        if x==y and y==c and c==d:
            return 0
        elif (x==y and y==c) or (x==y and y==d) or (x==c and c==d) or (d==y and y==c):
            print(i)
    for i in range(a,b+1):
        qqq(i)
for_4c(1000, 9999)

def for_5c(a, b, c, d): # Остатки
    a-=1
    x=(a-c+d)//d*d+c
    for i in range(x,b+1,d):
        print(i,end=' ')
for a in ((1, 100, 3, 33),(1, 100, 0, 25),(1, 100, 6, 7),(10, 100, 4, 50),(1, 100, 1, 2)):
    print()
    print(*a, end = "->")
    for_5c(*a)

def for_6c(n): # Потерянная карточка
    q=0
    for i in range(1,n+1):
        q+=i
    for j in range(n - 1):
        q-=int(input())
    print(q)

def for_7c(k): # Треугольная последовательность
    q=1
    for i in range(1,k+1):
        print(q,end='')
        if i == q*(q + 1) // 2:
             q += 1
for i in range(20):
    print()
    for_7c(i)


def for_8c(n): # Сумма факториалов
    def fact(n):
        f=1
        for i in range(1,n+1):
            f*=i
        return f
    k=1
    t=0
    while k!=n:
        t+=fact(k)
        k+=1
    return (t+fact(n))
for i in range(1,20):
    if not for_8c(i) == sum(math.factorial(j) for j in range(1, i+1)):
        print('\n Fail!', i, for_8c(i), sum(math.factorial(j) for j in range(i)), end='')