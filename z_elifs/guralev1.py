def elif1(int_number):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
    if int_number==1:
        return('понедельник')
    elif int_number==2:
        return('вторник')
    elif int_number==3:
        return('среда')
    elif int_number==4:
        return('четверг')
    elif int_number==5:
        return('пятница')
    elif int_number==6:
        return('суббота')
    elif int_number==7:
        return('воскресенье')
    else:
        return('0')


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
    """
    if k==1:
        return('Плохо')
    if k==2:
        return('Неудовлетворительно')
    if k==3:
        return('Удовлетворительно')
    if k==4:
        return('Хорошо')
    if k==5:
        return('Отлично')
    else:
        return('0')


def elif3(num_mounth):
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
    if num_mounth==9 or num_mounth==10 or num_mounth==11:
        return('Осень')
    elif num_mounth==12 or num_mounth==1 or num_mounth==2:
        return('Зима')
    elif num_mounth==3 or num_mounth==4 or num_mounth==5:
        return('Весна')
    elif num_mounth==6 or num_mounth==7 or num_mounth==8:
        return('Лето')
    else:
        return('ошибка')


def elif4(month):
     """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
     if month==1:
        return('31 день')
     elif month==2:
        return('28 дней')
     elif month==3:
        return('31 день')
     elif month==4:
        return('30 дней')
     elif month==5:
        return('31 день')
     elif month==6:
        return('30 дней')
     elif month==7:
        return('31 день')
     elif month==8:
        return('31 день')
     elif month==9:
        return('30 дней')
     elif month==10:
        return('31 день')
     elif month==11:
        return('30 дней')
     elif month==12:
        return('31 день')
     else:
        return('Такой даты нет')

def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия num (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    if n==1:
        return(a+b)
    elif n==2:
        return(a-b)
    elif n==3:
        return(a*b)
    elif n==4:
        return(a/b)
    else:
        return('ошибка')


def elif6(num, L):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    if num==1:
        return(L/10)
    elif num==2:
        return(L*1000)
    elif num==3:
        return(L)
    elif num==4:
        return(L/1000)
    elif num==5:
        return(L/100)
    else:
        return('ошибка')


def elif7(number, m):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
    if number==1:
        return(m)
    elif number==2:
        return(m/1000000)
    elif number==3:
        return(m/1000)
    elif number==4:
        return(m*1000)
    elif number==5:
        return(m*100)
    else:
        return('ошибка')