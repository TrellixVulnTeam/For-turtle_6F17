def elif1(int_namber):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
    if int_namber==1:
        return('Понеделиник')
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
        return('нет такого дня недели')


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «0».
    """
    if k==1:
        return('плохо')
    elif k==2:
        return('неудовлитворительно')
    elif k==3:
        return('удовлетворительно')
    elif k==4:
        return('хорошо')
    elif k==5:
        return('отлично')
    else:
        return('0')


def elif3(month):
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
    if 1<=month<=2 or month==12:
        return('Зима')
    elif 3<=month<=5:
        return('Весна')
    elif 6<=month<=8:
        return('Лето')
    elif 9<=month<=11:
        return('Осень')
    else:
        return('0')


def elif4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
    if (1<=month<=7 and month%2==1) or (8<=month<=12 and month%2==0):
        return('31')
    elif month==2:
        return('28')
    elif month==4 or month==6 or month==9 or month==11:
        return('30')


def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия num (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    if b==0:
        return('b не должно быть равно нулю')
    elif n==1:
        return('a+b=', a+b)
    elif n==2:
        return('a-b=', a-b)
    elif n==3:
        return('a*b=', a*b)
    elif n==4:
        return('a/b=', (a/b))


def elif6(number, length):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    if number==1:
        return('length-', length*0.1,'м',)
    elif number==2:
        return('length-', length*1000,'м',)
    elif number==3:
        return('length-', length,'м',)
    elif number==4:
        return('length-', length*0.001,'м',)
    elif number==5:
        return('length-', length*0.01,'м',)


def elif7(number, mass):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
    if number==1:
        return('mass-', mass,'кг',)
    elif number==2:
        return('mass-', mass/1000000,'кг',)
    elif number==3:
        return('mass-', mass*0.001,'кг',)
    elif number==4:
        return('mass-', mass*1000,'кг',)
    elif number==5:
        return('mass-', mass*100,'кг',)


def elif8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
    if month in (1,3,5,7,8,10,12):
        if day==1:
            if month==1:
                return('day-', 31, 'month-', 12)
            elif month==3:
                return('day-', 28, 'month-', 2)
            elif month==8:
                return('day-', 31, 'month-', 7)
            else:
                return('day-', 30, 'month-', month-1)
        elif day!=1 and day<=31:
            return('day-', day-1, 'month-', month)
        else:
            return('неправильная дата 0')
    elif month==2:
        if day==1:
            return('day-', 31, 'month-', 1)
        elif day!=1 and day<=28:
            return('day-', day-1, 'month-', month)
        else:
            return('неправильная дата 0')
    elif month in (4,6,9,11):
        if day==1:
            return('day-', 31, 'month-', month-1)
        elif day!=1 and day<=30:
            return('day-', day-1, 'month-', month)
        else:
            return('неправильная дата 0')


def elif9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
    if month in (1,3,5,7,8,10,12):
        if day==31:
            if month==12:
                return('day-', 1, 'month-', 1)
            else:
                return('day-', 1, 'month-', month+1)
        elif day!=31 and day<31:
            return('day-', day+1, 'month-', month)
        else:
            return('неправильная дата 0')
    elif month==2:
        if day==28:
            return('day-', 1, 'month-', 3)
        elif day!=28 and day<28:
            return('day-', day+1, 'month-', month)
        else:
            return('неправильная дата 0')
    elif month in (4,6,9,11):
        if day==30:
            return('day-', 1, 'month-', month+1)
        elif day!=30 and day<30:
            return('day-', day+1, 'month-', month)
        else:
            return('неправильная дата 0')


def elif10(symbol, int_namber):
    """
    Elif10. Робот может перемещаться в четырех направлениях («С» - С, «З» - З, «Ю» - Ю, «В» - В)
    и принимать три цифровые команды: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_namber - посланная ему команда.
    Вывести направление робота после выполнения полученной команды.
    """
    if symbol=='С':
        if int_namber==0:
            return('направление робота-', 'С')
        elif int_namber==1:
            return('направление робота-', 'З')
        elif int_namber==-1:
            return('направление робота-', 'В')
    elif symbol=='З':
        if int_namber==0:
            return('направление робота-', 'З')
        elif int_namber==1:
            return('направление робота-', 'Ю')
        elif int_namber==-1:
            return('направление робота-', 'С')
    elif symbol=='Ю':
        if int_namber==0:
            return('направление робота-', 'Ю')
        elif int_namber==1:
            return('направление робота-', 'В')
        elif int_namber==-1:
            return('направление робота-', 'З')
    elif symbol=='В':
        if int_namber==0:
            return('направление робота-', 'В')
        elif int_namber==1:
            return('направление робота-', 'С')
        elif int_namber==-1:
            return('направление робота-', 'Ю')


def elif11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - С, «З» - З, «Ю» - Ю, «В» - В)
    и может принимать три цифровые команды поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные команды.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    if symbol=='С':
        if int1==1:
            if int2==1:
                return('направление робота-', 'Ю')
            elif int2==-1:
                return('направление робота-', 'С')
            elif int2==2:
                return('направление робота-', 'В')
        elif int1==-1:
            if int2==1:
                return('направление робота-', 'С')
            elif int2==-1:
                return('направление робота-', 'Ю')
            elif int2==2:
                return('направление робота-', 'З')
        elif int1==2:
            if int2==1:
                return('направление робота-', 'В')
            elif int2==-1:
                return('направление робота-', 'З')
            elif int2==2:
                return('направление робота-', 'С')
    elif symbol=='З':
        if int1==1:
            if int2==1:
                return('направление робота-', 'В')
            elif int2==-1:
                return('направление робота-', 'З')
            elif int2==2:
                return('направление робота-', 'С')
        elif int1==-1:
            if int2==1:
                return('направление робота-', 'З')
            elif int2==-1:
                return('направление робота-', 'В')
            elif int2==2:
                return('направление робота-', 'Ю')
        elif int1==2:
            if int2==1:
                return('направление робота-', 'С')
            elif int2==-1:
                return('направление робота-', 'Ю')
            elif int2==2:
                return('направление робота-', 'З')

    elif symbol=='Ю':
        if int1==1:
            if int2==1:
                return('направление робота-', 'С')
            elif int2==-1:
                return('направление робота-', 'Ю')
            elif int2==2:
                return('направление робота-', 'З')
        elif int1==-1:
            if int2==1:
                return('направление робота-', 'Ю')
            elif int2==-1:
                return('направление робота-', 'С')
            elif int2==2:
                return('направление робота-', 'В')
        elif int1==2:
            if int2==1:
                return('направление робота-', 'З')
            elif int2==-1:
                return('направление робота-', 'В')
            elif int2==2:
                return('направление робота-', 'Ю')

    elif symbol=='В':
        if int1==1:
            if int2==1:
                return('направление робота-', 'З')
            elif int2==-1:
                return('направление робота-', 'В')
            elif int2==2:
                return('направление робота-', 'Ю')
        elif int1==-1:
            if int2==1:
                return('направление робота-', 'В')
            elif int2==-1:
                return('направление робота-', 'З')
            elif int2==2:
                return('направление робота-', 'С')
        elif int1==2:
            if int2==1:
                return('направление робота-', 'Ю')
            elif int2==-1:
                return('направление робота-', 'С')
            elif int2==2:
                return('направление робота-', 'В')