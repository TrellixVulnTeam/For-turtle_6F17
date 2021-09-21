def elif1(int_namber):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
    if int_namber == 1:
        return('понедельник')
    elif int_namber == 2:
        return('вторник')
    elif int_namber == 3:
        return('среда')
    elif int_namber == 4:
        return('четверг')
    elif int_namber == 5:
        return('пятница')
    elif int_namber == 6:
        return('суббота')
    elif int_namber == 7:
        return('воскресенье')
    else:
        return('Неверное введено число')


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
    """
    if k==1:
        return('плохо')
    elif k==2:
        return('неудовлетворительно')
    elif k==3:
        return('удовлетворительно')
    elif k==4:
        return('хорошо')
    elif k==5:
        return('отлично')
    else:
        return('ошибка')


def elif3(month):
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
    if month in [12,1,2]:
        return("зима")
    elif month in [3,4,5]:
        return('весна')
    elif month in [6,7,8]:
        return('лето')
    elif month in [9,10,11]:
        return('осень')
    else:
        return('Нету такого месяца')


def elif4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
    if month in [1,3,5,7,8,10,12]:
        return(31)
    elif month in [4,6,9,11]:
        return(30)
    elif month==2:
        return(28)
    else:
        return('Нет такого месяца')


def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия num (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    if n==1: 
        return(a,'+',b,'=',a+b) 
    elif n==2: 
        return(a,'-',b,'=',a-b) 
    elif n==3: 
        return(a,'*',b,'=',a*b) 
    elif n==4 and b!=0: 
        return(a,'/',b,'=',a/b) 
    else: 
        return('неверное условие')


def elif6(number, length):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    if number==1: 
        return(length,'дм= ',length/10,'м') 
    elif number==2: 
        return(length,'км= ',length*1000,'м') 
    elif number==3: 
        return(length,'м= ',length,'м') 
    elif number==4: 
        return(length,'мм= ',length/1000,'м') 
    elif number==5: 
        return(length,'см= ',length/100,'м') 
    else: 
        return('Не правильное значение number')


def elif7(number, mass):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
    if number==1: 
        return(mass,'кг = ',mass,'кг') 
    elif number==2: 
        return(mass,'мг = ',mass/1000000,'кг') 
    elif number==3: 
        return(mass,'г = ',mass/1000,'кг') 
    elif number==4: 
        return(mass,'т = ',mass*1000,'кг') 
    elif number==5: 
        return(mass,'ц = ',mass*100,'кг') 
    else: 
        return('Не правильное значение number')



def elif8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
    if day==1: 
        if month==3: 
            day=28 
        elif month in [5,7,10,12]: 
            day=30 
        elif month in [1,2,4,6,8,9,11]: 
            day=31 
        month=(month+10)%12+1 
    else: 
        day-=1 
    return(day,'.',month)


def elif9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
    mday = None
    if month==2:
        mday=28 
    elif month in (4,6,9,11):
        mday=30 
    elif month in (1,3,5,7,8,10,12):
        mday=31 

    if day<mday:
        day+=1 
    else: 
        month=month%12+1 
        day=1 
    return(day,'.',month)



def elif10(symbol, int_namber):
    """
    Elif10. Робот может перемещаться в четырех направлениях («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и принимать три цифровые команды: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_namber - посланная ему команда.
    Вывести направление робота после выполнения полученной команды.
    """
    if int_namber==-1:
        if symbol=='С': 
            symbol='В' 
        elif symbol=='З': 
            symbol='С' 
        elif symbol=='Ю': 
            symbol='З' 
        elif symbol=='В': 
            symbol='Ю' 
    elif int_namber==1:
        if symbol=='С': 
            symbol='З' 
        elif symbol=='З': 
            symbol='Ю' 
        elif symbol=='Ю': 
            symbol='В' 
        elif symbol=='В': 
            symbol='С' 
    elif int_namber==0:
        symbol=symbol 
    else: 
        symbol='Не верная команда' 
    return(symbol)



def elif11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и может принимать три цифровые команды поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные команды.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    def r(int,symbol):
        if int==-1:
            if symbol=='С':
                symbol='В'
            elif symbol=='З':
                symbol='С'
            elif symbol=='Ю':
                symbol='З'
            elif symbol=='В':
                symbol='Ю'
        elif int==1:
            if symbol=='С':
                symbol='З'
            elif symbol=='З':
                symbol='Ю'
            elif symbol=='Ю':
                symbol='В'
            elif symbol=='В':
                symbol='С'
        elif int==2:
            if symbol=='С':
                symbol='Ю'
            elif symbol=='З':
                symbol='В'
            elif symbol=='Ю':
                symbol='В'
            elif symbol=='В':
                symbol='С'
        return symbol
    symbol= r(int1, symbol)
    symbol= r(int2, symbol)
    return(symbol)