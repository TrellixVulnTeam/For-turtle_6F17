def elif1(int_namber):
    if int_namber==1:
        return('Понедельник')
    elif int_namber==2:
        return('Вторник')
    elif int_namber==3:
        return('Среда')
    elif int_namber==4:
        return('Четверг')
    elif int_namber==5:
        return('Пятница')
    elif int_namber==6:
        return('Суббота')
    elif int_namber==7:
        return('Воскресенье')
    else:
        return('Неправильный ввод числа')


def elif2(k):
    if k==1:
        return('Плохо')
    elif k==2:
        return('Неудовлетворительно')
    elif k==3:
        return('Удовлетворительно')
    elif k==4:
        return('Хорошо')
    elif k==5:
        return('Отлично')
    else:
        return('0')


def elif3(month):
    if month in (12,1,2):
        return('Зима')
    elif month in (3,4,5):
        return('Весна')
    elif month in (6,7,8):
        return('Лето')
    elif month in (9,10,11):
        return('Осень')
    else:
        return('0')


def elif4(month):
    if month in (1,3,5,7,8,10,12):
        return('31')
    elif month in (4,6,9,11):
        return("30")
    elif month==2:
        return('28')


def elif5(n, a, b):
    if n==1:
        return(a+b)
    elif n==2:
        return(a-b)
    elif n==3:
        return(a*b)
    elif n==4:
        return(a/b)
    else:
        return('Неправильный ввод числа')

def elif6(number, length):
    if number==1:
        return(length/10)
    elif number==2:
        return(length*1000)
    elif number==3:
        return(length)
    elif number==4:
        return(length/1000)
    elif number==5:
        return(length/100)

def elif7(number, mass):
    if number==1:
        return(mass)
    elif number==2:
        return(mass/1000000)
    elif number==3:
        return(mass/1000)
    elif number==4:
        return(mass*1000)
    elif number==5:
        return(mass*100)
    else:
        return('0')


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
        day=month='0'
    return(day,month)


def elif9(day,month):
    if month in (1,3,5,7,8,10) and day==31:
        return(f'day - 1, month - {month+1}')
    elif month in (4,6,9,11) and day==30:
        return(f'day - 1, month - {month+1}')
    elif month==2 and day==28:
        return(f'day - 1, month - {month+1}')
    elif month in (4,6,9,11) and 1<=day<30:
        return(f'day - {day+1}, month - {month}')
    elif month in (1,3,5,7,8,10) and 1<=day<31:
        return(f'day - {day+1}, month - {month}')
    elif month==2 and 1<=day<28:
        return(f'day - {day+1}, month - {month}')
    elif month==12 and day==31:
        return('day - 1, month - 1')
    elif month==12 and day!=31 and 1<=day:
        return(f'day - {day+1}, month - {month}')
    else:
        return('0')


def elif10(symbol, int_namber):
    if int_namber==0:
        return(symbol)
    elif int_namber==1:
        if symbol=='С':
            return('З')
        elif symbol=='З':
            return('Ю')
        elif symbol=='Ю':
            return('В')
        elif symbol=='В':
            return('С')
    elif int_namber==-1:
        if symbol=='С':
            return('В')
        elif symbol=='В':
            return('Ю')
        elif symbol=='Ю':
            return('З')
        elif symbol=='З':
            return('С')
    else:
        return('0')

def elif11(symbol, int1, int2):
    if symbol not in ('Ю','З','В','С') or int1 not in (1,-1,2) or int2 not in (1,-1,2):
        return('0')
    elif int1==2:
        if int2==1:
            if symbol=='С':
                return('В')
            elif symbol=='З':
                return('С')
            elif symbol=='Ю':
                return('З')
            elif symbol=='В':
                return('Ю')
        elif int2==2:
            return(symbol)
        elif int2==-1:
            if symbol=='С':
                return('З')
            elif symbol=='З':
                return('Ю')
            elif symbol=='Ю':
                return('В')
            elif symbol=='В':
                return('С')
    elif int1==1:
        if int2==1:
            if symbol=='С':
                return('Ю')
            elif symbol=='З':
                return('В')
            elif symbol=='Ю':
                return('С')
            elif symbol=='В':
                return('З')
        elif int2==-1:
            return(symbol)
        elif int2==2:
            if symbol=='С':
                return('В')
            elif symbol=='З':
                return('С')
            elif symbol=='Ю':
                return('З')
            elif symbol=='В':
                return('Ю')            
    elif int1==-1:
        if int2==1:
            return(symbol)
        elif int2==-1:
            if symbol=='С':
                return('Ю')
            elif symbol=='В':
                return('З')
            elif symbol=='Ю':
                return('С')
            elif symbol=='З':
                return('В')
        elif int2==2:
            if symbol=='С':
                return('З')
            elif symbol=='В':
                return('С')
            elif symbol=='Ю':
                return('В')
            elif symbol=='З':
                return('Ю')   