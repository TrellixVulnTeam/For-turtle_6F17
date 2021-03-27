def elif1(int_number):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
    if int_number==1:
        return('Понедельник')
    elif int_number==2:
        return('Вторник')
    elif int_number==3:
        return('Среда')
    elif int_number==4:
        return('Четверг')
    elif int_number==5:
        return('Пятница')
    elif int_number==6:
        return('Суббота')
    elif int_number==7:
        return('Воскресенье')
    else:
        return('0 дата')


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «0».
    """
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
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
    if month==12 or 1<=month<=2:
        return('Зима')
    elif 3<=month<=5:
        return('Весна')
    elif 6<=month<=8:
        return('Лето')
    elif 9<=month<=11:
        return('Осень')
    else:
        return('0 дата')


def elif4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
    month_l=(1,3,5,7,8,10,12)
    month_s=(4,6,9,11)
    if month in month_l:
        return('31 день')
    elif month in month_s:
        return('30 дней')
    elif month==2:
        return('28 дней')
    else:
        return('0')


def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия n (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    if b==0:
        return('b не равно 0')
    elif n==1:
        return(a+b)
    elif n==2:
        return(a-b)
    elif n==3:
        return(a*b)
    elif n==4:
        return(a/b)
    else:
        return('0 действия нет')


def elif6(number, length):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    if number==1:
        return(length/10)
    elif number==2:
        return(length*1000)
    elif number==3:
        return(length*1)
    elif number==4:
        return(length*0.001)
    elif number==5:
        return(length*0.01)
    else:
        return('Такой единицы длины нет')


def elif7(number, mass):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
    if number==1:
        return(mass*1)
    elif number==2:
        return(mass/1000000)
    elif number==3:
        return(mass*0.001)
    elif number==4:
        return(mass*1000)
    elif number==5:
        return(mass*100)
    else:
        return('Такой единицы массы нет')


def elif8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
    month_l=(1,3,5,7,8,10,12)
    month_s=(4,6,9,11)
    if day==1:
        if month==1:
            return(31,12)
        elif month==2:
            return(31,1)
        elif month==3:
            return(28,2)
        elif month in month_l:
            return(31,month-1)
        elif month in month_s:
            return(30,month-1)
        else:
            return('0 0')
    elif month in month_l:
        if 1<day<=31:
            return(day-1,month)
        else:
            return('0 0')
    elif month in month_s:
        if 1<day<=30:
            return(day-1,month)
        else:
            return('0 0')
    elif month==2:
        if 1<day<=28:
            return(day-1,month)
        else:
            return('0 0')
    else:
        return('0 0')

def elif9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
    month_l=(1,3,5,7,8,10,12)
    month_s=(4,6,9,11)
    if day==31:
        if month==12:
            return(1,1)
        elif month in month_l:
            return(1,month+1)
        else:
            return('0 дата')
    elif day==30:
        if month in month_s:
            return(1,month+1)
        elif month in month_l:
            return(day+1,month)
        else:
            return('0 дата')
    elif day==28:
        if month==2:
            return(1,month+1)
        elif month in month_l:
            return(day+1,month)
        elif month in month_s:
            return(day+1,month)
        else:
            return('0 дата')
    elif month in month_l:
        if 1<=day<31:
            return(day+1,month)
        else:
            return('0 дата')
    elif month in month_s:
        if 1<=day<30:
            return(day+1,month)
        else:
            return('0 дата')
    elif month==2:
        if 1<=day<28:
            return(day+1,month)
        else:
            return('0 дата')
    else:
        return('0 дата')


def elif10(symbol, int_namber):
    """
    Elif10. Робот может перемещаться в четырех направлениях («С» - С, «З» - З, «Ю» - Ю, «В» - В)
    и принимать три цифровые 0: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_namber - посланная ему команда.
    Вывести направление робота после выполнения полученной 0.
    """
    if symbol in ('С','Ю','З','В'):
        if symbol=='С':
            if int_namber==0:
                return('С')
            elif int_namber==1:
                return('З')
            elif int_namber==-1:
                return('В')
            else:
                return('Такой 0 нет')
        elif symbol=='Ю':
            if int_namber==0:
                return('Ю')
            elif int_namber==1:
                return('В')
            elif int_namber==-1:
                return('З')
            else:
                return('Такой 0 нет') 
        elif symbol=='З':
            if int_namber==0:
                return('З')
            elif int_namber==1:
                return('Ю')
            elif int_namber==-1:
                return('С')
            else:
                return('Такой 0 нет')
        elif symbol=='В':
            if int_namber==0:
                return('В')
            elif int_namber==1:
                return('С')
            elif int_namber==-1:
                return('Ю')
            else:
                return('Такой 0 нет')
    else:
        return('0 направления нет')


def elif11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - С, «З» - З, «Ю» - Ю, «В» - В)
    и может принимать три цифровые 0 поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные 0.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    if symbol in ('С','Ю','З','В'):
        if symbol=='С':
            if int1==-1:
                if int2==-1:
                    return('Ю')
                elif int2==1:
                    return('С')
                elif int2==2:
                    return('В')
                else:
                    return('0')
            elif int1==1:
                if int2==-1:
                    return('С')
                elif int2==1:
                    return('Ю')
                elif int2==2:
                    return('З')
                else:
                    return('0')
            elif int1==2:
                if int2==-1:
                    return('В')
                elif int2==1:
                    return('З')
                elif int2==2:
                    return('С')
                else:
                    return('Такой 0 нет')
            else:
                return('Такой 0 нет')
        elif symbol=='Ю':
            if int1==-1:
                if int2==-1:
                    return('С')
                elif int2==1:
                    return('Ю')
                elif int2==2:
                    return('З')
                else:
                    return('Такой 0 нет')
            elif int1==1:
                if int2==-1:
                    return('Ю')
                elif int2==1:
                    return('С')
                elif int2==2:
                    return('В')
                else:
                    return('Такой 0 нет')
            elif int1==2:
                if int2==-1:
                    return('З')
                elif int2==1:
                    return('В')
                elif int2==2:
                    return('Ю')
                else:
                    return('Такой 0 нет')
            else:
                return('Такой 0 нет')
        elif symbol=='З':
            if int1==-1:
                if int2==-1:
                    return('В')
                elif int2==1:
                    return('З')
                elif int2==2:
                    return('С')
                else:
                    return('Такой 0 нет')
            elif int1==1:
                if int2==-1:
                    return('З')
                elif int2==1:
                    return('В')
                elif int2==2:
                    return('Ю')
                else:
                    return('Такой 0 нет')
            elif int1==2:
                if int2==-1:
                    return('С')
                elif int2==1:
                    return('Ю')
                elif int2==2:
                    return('З')
                else:
                    return('Такой 0 нет')
            else:
                return('Такой 0 нет')
        elif symbol=='В':
            if int1==-1:
                if int2==-1:
                    return('З')
                elif int2==1:
                    return('В')
                elif int2==2:
                    return('Ю')
                else:
                    return('Такой 0 нет')
            elif int1==1:
                if int2==-1:
                    return('В')
                elif int2==1:
                    return('З')
                elif int2==2:
                    return('С')
                else:
                    return('Такой 0 нет')
            elif int1==2:
                if int2==-1:
                    return('Ю')
                elif int2==1:
                    return('С')
                elif int2==2:
                    return('В')
                else:
                    return('Такой 0 нет')
            else:
                return('Такой 0 нет')
        else:
            return('0 направления нет')