def elif1(int_namber):
    if int_namber==1:
        print('Понедельник')
    elif int_namber==2:
        print('Вторник')
    elif int_namber==3:
        print('Среда')
    elif int_namber==4:
        print('Четверг')
    elif int_namber==5:
        print('Пятница')
    elif int_namber==6:
        print('Суббота')
    elif int_namber==7:
        print('Воскресенье')
    else:
        print('Неправильный ввод числа')


def elif2(k):
    if k==1:
        print('Плохо')
    elif k==2:
        print('Неудовлетворительно')
    elif k==3:
        print('Удовлетворительно')
    elif k==4:
        print('Хорошо')
    elif k==5:
        print('Отлично')
    else:
        print('Ошибка')


def elif3(month):
    if month in (12,1,2):
        print('Зима')
    elif month in (3,4,5):
        print('Весна')
    elif month in (6,7,8):
        print('Лето')
    elif month in (9,10,11):
        print('Осень')
    else:
        print('Ошибка')


def elif4(month):
    if month in (1,3,5,7,8,10,12):
        print('31')
    elif month in (4,6,9,11):
        print("30")
    elif month==2:
        print('28')


def elif5(n, a, b):
    if n==1:
        print(a+b)
    elif n==2:
        print(a-b)
    elif n==3:
        print(a*b)
    elif n==4:
        print(a/b)
    else:
        print('Неправильный ввод числа')

def elif6(number, length):
    if number==1:
        print(length/10)
    elif number==2:
        print(length*1000)
    elif number==3:
        print(length)
    elif number==4:
        print(length/1000)
    elif number==5:
        print(length/100)

def elif7(number, mass):
    if number==1:
        print(mass)
    elif number==2:
        print(mass/1000000)
    elif number==3:
        print(mass/1000)
    elif number==4:
        print(mass*1000)
    elif number==5:
        print(mass*100)
    else:
        print('Ошибка')


def elif8(day,month):
    if month in (5,7,10,12) and day==1:
        day=30
        month=month-1
    elif month in (2,4,6,8,9,11) and day==1:
        month=month-1
        day=31
    elif month==3 and day==1:
        day=28
        month=month-1
    elif month==2 and 1<day<=28:
        day=day-1
    elif month in (1,3,5,7,8,10,12) and 1<day<=31:
        day=day-1
    elif month in (4,6,9,11) and 1<day<=30:
        day=day-1
    elif month==1 and day==1:
        day=31
        month=12
    else:
        day=month='Ошибка'
    print(day,month)


def elif9(day,month):
    if month in (1,3,5,7,8,10) and day==31:
        print(f'day - 1, month - {month+1}')
    elif month in (4,6,9,11) and day==30:
        print(f'day - 1, month - {month+1}')
    elif month==2 and day==28:
        print(f'day - 1, month - {month+1}')
    elif month in (4,6,9,11) and 1<=day<30:
        print(f'day - {day+1}, month - {month}')
    elif month in (1,3,5,7,8,10) and 1<=day<31:
        print(f'day - {day+1}, month - {month}')
    elif month==2 and 1<=day<28:
        print(f'day - {day+1}, month - {month}')
    elif month==12 and day==31:
        print('day - 1, month - 1')
    elif month==12 and day!=31 and 1<=day:
        print(f'day - {day+1}, month - {month}')
    else:
        print('Ошибка')


def elif10(symbol, int_namber):
    if int_namber==0:
        print(symbol)
    elif int_namber==1:
        if symbol=='С':
            print('З')
        elif symbol=='З':
            print('Ю')
        elif symbol=='Ю':
            print('В')
        elif symbol=='В':
            print('С')
    elif int_namber==-1:
        if symbol=='С':
            print('В')
        elif symbol=='В':
            print('Ю')
        elif symbol=='Ю':
            print('З')
        elif symbol=='З':
            print('С')
    else:
        print('Ошибка')

def elif11(symbol, int1, int2):
    if symbol not in ('Ю','З','В','С') or int1 not in (1,-1,2) or int2 not in (1,-1,2):
        print('Ошибка')
    elif int1==2:
        if int2==1:
            if symbol=='С':
                print('В')
            elif symbol=='З':
                print('С')
            elif symbol=='Ю':
                print('З')
            elif symbol=='В':
                print('Ю')
        elif int2==2:
            print(symbol)
        elif int2==-1:
            if symbol=='С':
                print('З')
            elif symbol=='З':
                print('Ю')
            elif symbol=='Ю':
                print('В')
            elif symbol=='В':
                print('С')
    elif int1==1:
        if int2==1:
            if symbol=='С':
                print('Ю')
            elif symbol=='З':
                print('В')
            elif symbol=='Ю':
                print('С')
            elif symbol=='В':
                print('З')
        elif int2==-1:
            print(symbol)
        elif int2==2:
            if symbol=='С':
                print('В')
            elif symbol=='З':
                print('С')
            elif symbol=='Ю':
                print('З')
            elif symbol=='В':
                print('Ю')            
    elif int1==-1:
        if int2==1:
            print(symbol)
        elif int2==-1:
            if symbol=='С':
                print('Ю')
            elif symbol=='В':
                print('З')
            elif symbol=='Ю':
                print('С')
            elif symbol=='З':
                print('В')
        elif int2==2:
            if symbol=='С':
                print('З')
            elif symbol=='В':
                print('С')
            elif symbol=='Ю':
                print('В')
            elif symbol=='З':
                print('Ю')   