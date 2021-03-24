def elif1(int_number):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
    if int_number==1:
        print('Понедельник')
    elif int_number==2:
        print('Вторник')
    elif int_number==3:
        print('Среда')
    elif int_number==4:
        print('Четверг')
    elif int_number==5:
        print('Пятница')
    elif int_number==6:
        print('Суббота')
    elif int_number==7:
        print('Воскресенье')
    else:
        print('Неверная дата')


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
    """
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
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
    if month==12 or 1<=month<=2:
        print('Зима')
    elif 3<=month<=5:
        print('Весна')
    elif 6<=month<=8:
        print('Лето')
    elif 9<=month<=11:
        print('Осень')
    else:
        print('Неверная дата')


def elif4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
    month_l=(1,3,5,7,8,10,12)
    month_s=(4,6,9,11)
    if month in month_l:
        print('31 день')
    elif month in month_s:
        print('30 дней')
    elif month==2:
        print('28 дней')
    else:
        print('Неверная дата')


def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия n (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    if b==0:
        print('b не равно 0')
    elif n==1:
        print(a+b)
    elif n==2:
        print(a-b)
    elif n==3:
        print(a*b)
    elif n==4:
        print(a/b)
    else:
        print('Такого действия нет')


def elif6(number, length):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    if number==1:
        print(length/10)
    elif number==2:
        print(length*1000)
    elif number==3:
        print(length*1)
    elif number==4:
        print(length*0.001)
    elif number==5:
        print(length*0.01)
    else:
        print('Такой единицы длины нет')


def elif7(number, mass):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
    if number==1:
        print(mass*1)
    elif number==2:
        print(mass/1000000)
    elif number==3:
        print(mass*0.001)
    elif number==4:
        print(mass*1000)
    elif number==5:
        print(mass*100)
    else:
        print('Такой единицы массы нет')


def elif8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
    month_l=(1,3,5,7,8,10,12)
    month_s=(4,6,9,11)
    if day==1:
        if month==1:
            print(31,12)
        elif month==2:
            print(31,1)
        elif month==3:
            print(28,2)
        elif month in month_l:
            print(31,month-1)
        elif month in month_s:
            print(30,month-1)
        else:
            print('Неверная дата')
    elif month in month_l:
        if 1<day<=31:
            print(day-1,month)
        else:
            print('Неверная дата')
    elif month in month_s:
        if 1<day<=30:
            print(day-1,month)
        else:
            print('Неверная дата')
    elif month==2:
        if 1<day<=28:
            print(day-1,month)
        else:
            print('Неверная дата')
    else:
        print('Неверная дата')

def elif9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
    month_l=(1,3,5,7,8,10,12)
    month_s=(4,6,9,11)
    if day==31:
        if month==12:
            print(1,1)
        elif month in month_l:
            print(1,month+1)
        else:
            print('Неверная дата')
    elif day==30:
        if month in month_s:
            print(1,month+1)
        elif month in month_l:
            print(day+1,month)
        else:
            print('Неверная дата')
    elif day==28:
        if month==2:
            print(1,month+1)
        elif month in month_l:
            print(day+1,month)
        elif month in month_s:
            print(day+1,month)
        else:
            print('Неверная дата')
    elif month in month_l:
        if 1<=day<31:
            print(day+1,month)
        else:
            print('Неверная дата')
    elif month in month_s:
        if 1<=day<30:
            print(day+1,month)
        else:
            print('Неверная дата')
    elif month==2:
        if 1<=day<28:
            print(day+1,month)
        else:
            print('Неверная дата')
    else:
        print('Неверная дата')


def elif10(symbol, int_namber):
    """
    Elif10. Робот может перемещаться в четырех направлениях («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и принимать три цифровые команды: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_namber - посланная ему команда.
    Вывести направление робота после выполнения полученной команды.
    """
    if symbol in ('С','Ю','З','В'):
        if symbol=='С':
            if int_namber==0:
                print('Север')
            elif int_namber==1:
                print('Запад')
            elif int_namber==-1:
                print('Восток')
            else:
                print('Такой команды нет')
        elif symbol=='Ю':
            if int_namber==0:
                print('Юг')
            elif int_namber==1:
                print('Восток')
            elif int_namber==-1:
                print('Запад')
            else:
                print('Такой команды нет') 
        elif symbol=='З':
            if int_namber==0:
                print('Запад')
            elif int_namber==1:
                print('Юг')
            elif int_namber==-1:
                print('Север')
            else:
                print('Такой команды нет')
        elif symbol=='В':
            if int_namber==0:
                print('Восток')
            elif int_namber==1:
                print('Север')
            elif int_namber==-1:
                print('Юг')
            else:
                print('Такой команды нет')
    else:
        print('Такого направления нет')


def elif11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и может принимать три цифровые команды поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные команды.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    if symbol in ('С','Ю','З','В'):
        if symbol=='С':
            if int1==-1:
                if int2==-1:
                    print('Юг')
                elif int2==1:
                    print('Север')
                elif int2==2:
                    print('Восток')
                else:
                    print('Такой команды нет')
            elif int1==1:
                if int2==-1:
                    print('Север')
                elif int2==1:
                    print('Юг')
                elif int2==2:
                    print('Запад')
                else:
                    print('Такой команды нет')
            elif int1==2:
                if int2==-1:
                    print('Восток')
                elif int2==1:
                    print('Запад')
                elif int2==2:
                    print('Север')
                else:
                    print('Такой команды нет')
            else:
                print('Такой команды нет')
        elif symbol=='Ю':
            if int1==-1:
                if int2==-1:
                    print('Север')
                elif int2==1:
                    print('Юг')
                elif int2==2:
                    print('Запад')
                else:
                    print('Такой команды нет')
            elif int1==1:
                if int2==-1:
                    print('Юг')
                elif int2==1:
                    print('Север')
                elif int2==2:
                    print('Восток')
                else:
                    print('Такой команды нет')
            elif int1==2:
                if int2==-1:
                    print('Запад')
                elif int2==1:
                    print('Восток')
                elif int2==2:
                    print('Юг')
                else:
                    print('Такой команды нет')
            else:
                print('Такой команды нет')
        elif symbol=='З':
            if int1==-1:
                if int2==-1:
                    print('Восток')
                elif int2==1:
                    print('Запад')
                elif int2==2:
                    print('Север')
                else:
                    print('Такой команды нет')
            elif int1==1:
                if int2==-1:
                    print('Запад')
                elif int2==1:
                    print('Восток')
                elif int2==2:
                    print('Юг')
                else:
                    print('Такой команды нет')
            elif int1==2:
                if int2==-1:
                    print('Север')
                elif int2==1:
                    print('Юг')
                elif int2==2:
                    print('Запад')
                else:
                    print('Такой команды нет')
            else:
                print('Такой команды нет')
        elif symbol=='В':
            if int1==-1:
                if int2==-1:
                    print('Запад')
                elif int2==1:
                    print('Восток')
                elif int2==2:
                    print('Юг')
                else:
                    print('Такой команды нет')
            elif int1==1:
                if int2==-1:
                    print('Восток')
                elif int2==1:
                    print('Запад')
                elif int2==2:
                    print('Север')
                else:
                    print('Такой команды нет')
            elif int1==2:
                if int2==-1:
                    print('Юг')
                elif int2==1:
                    print('Север')
                elif int2==2:
                    print('Восток')
                else:
                    print('Такой команды нет')
            else:
                print('Такой команды нет')
        else:
            print('Такого направления нет')