def elif1(int_namber):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
    if int_namber == 1:
        print("пн")
    elif int_namber == 2:
        print("вт")
    elif int_namber == 3:
        print("ср")
    elif int_namber == 4:
        print("чт")
    elif int_namber == 5:
        print("пт")
    elif int_namber == 6:
        print("сб")
    elif int_namber == 7:
        print("вс")
    else:
        print("не подходит")


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
    """
    if k == 1:
        print("плохо")
    elif k ==2:
        print("неудовлетворительно")
    elif k ==3:
        print("удовлетворительно")
    elif k ==4:
        print("хорошо")
    elif k ==5:
        print("отлично")
    else:
        print("ошибка")

    
    


def elif3(month):
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
    if month in (1,2,12):
        print("зима")
    elif month in (3,4,5):
        print("весна")
    elif month in (6,7,8):
        print("лето")
    elif month in (9,10,11):
        print("осень")


def elif4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
    if month in (1,3,5,7,8,10,12):
        print(31)
    elif month in (4,6,9,11):
        print(30)
    elif month == 2:
        print(28)



def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия n (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    if n == 1:
        print(a+b)
    elif n == 2:
        print(a-b)
    elif n == 3:
        print(a*b)
    elif n == 4:
        print(a//b)


def elif6(number, length):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    if number==1:
        print(length/10)
    elif number== 2:
        print(length*1000)
    elif number== 3:
        print(length)
    elif number== 4:
        print(length/1000)
    elif number== 5:
        print(length/100)

def elif7(number, mass):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
    if number==1:
        print(mass)
    elif number== 2:
        print(mass/1000000)
    elif number== 3:
        print(mass/1000)
    elif number== 4:
        print(mass*1000)
    elif number== 5:
        print(mass*100)


def elif8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
    if month == 1 and day == 1:
        print(31, 12)
    elif month > 1:
        if day>1:
            print(day-1, month)
        elif day == 1:
            if month in (5,7,10,12):
                print(30, month-1)
            elif month in (2,4,6,9,11,1):
                print(31, month-1)
            elif month == 3:
                print(28, month-1)


def elif9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
    if month == 12 and day == 31:
        print(1, 1)
elif month in (1,3,5,7,8,10,12):
    if day<31:
        print(day+1,month)
    elif day == 31:
        print(1, month+1)
elif month in (4,6,9,11):
    if day<30:
        print(day+1,month)
    elif day == 30:
        print(1, month+1)
elif month == 2:
    if day<28:
        print(day+1,month)
    elif day == 28:
        print(1, month+1)


def elif10(symbol, int_namber):
    """
    Elif10. Робот может перемещаться в четырех направлениях («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и принимать три цифровые команды: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_namber - посланная ему команда.
    Вывести направление робота после выполнения полученной команды.
    """
    if symbol=="С":
        if int_namber == 0:
            print("С")
        elif int_namber==1:
            print("В")
        elif int_namber==-1:
            print("З")
    elif symbol=="В":
        if int_namber == 0:
            print("В")
        elif int_namber==1:
            print("Ю")
        elif int_namber==-1:
            print("С")
    elif symbol=="Ю":
        if int_namber == 0:
            print("Ю")
        elif int_namber==1:
            print("В")
        elif int_namber==-1:
            print("З")
    elif symbol=="З":
        if int_namber == 0:
            print("З")
        elif int_namber==1:
            print("С")
        elif int_namber==-1:
            print("Ю")
    


def elif11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и может принимать три цифровые команды поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные команды.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    