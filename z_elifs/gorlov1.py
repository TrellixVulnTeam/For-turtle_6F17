def elif1(int_namber):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
    if int_namber==1:
        return('пн')
    elif int_namber==2:
        return('вт')
    elif int_namber==3:
        return('ср')
    elif int_namber==4:
        return('чт')
    elif int_namber==5:
        return('пт')
    elif int_namber==6:
        return('сб')
    elif int_namber==7:
        return('вс')


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «0».
    """
    if k==1:
        return('плохо')
    elif k==2:
        return('неудовлетворитльно')
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
    if month  in(1,2,12):
        return('зима')
    elif month in(3,4,5):
        return('весна')
    elif month in(6,7,8):
        return('лето')
    elif month in(9,10,11):
        return('осень')


def elif4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
    if month in(1,3,5,7,9,11):
        return(31)
    elif month in(4,6,8,10,12):
        return(30)
    elif month == 2:
        return(28)


def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия num (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    mat=0
    if b==0:
        return('b не равно 0!')
    elif n == 1:
        mat=a+b
    elif n == 2:
        mat=a-b
    elif n == 3:
        mat=a*b
    elif n == 4:
        mat=a/b
    return(mat)
    

def elif6(length, number):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    m = 0
    if length<0:
        return('0')
    elif length == 0:
        return(0)
    elif length == 1:
        m = number/10
    elif length == 2:
        m = number*1000
    elif length == 3:
        m = number
    elif length == 4:
        m = number/1000
    elif length == 5:
        m = number/100
    return(m)


def elif7(mass, number):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
    m = None
    if mass<0:
        return('0')
    elif mass == 0:
        return(0)
    elif mass == 1:
        m = number
    elif mass == 2:
        m = number/1000000
    elif mass == 3:
        m = number/1000
    elif mass == 4:
        m = number*1000
    elif mass == 5:
        m = number*100
    return(m)


def elif8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
    if month==2 and day>=29:
        return('0')
    elif month in(1,5,7,9,11): 
        if day>1:
            return(f'month = {month} day = {day-1}')
        elif day==1:
            return(f'month = {month-1} day = {30}')
    elif month in(2,4,6,8,10,12):
        if 1<day<31:
            return(f'month = {month} day = {day-1}')
        elif day==1:
            return(f'month = {month-1} day = {31}')
        elif day>=31:
            return('0')
    elif month == 3:   
        if day>1:
            return(f'month = {month} day = {day-1}')
        elif day==1:
            return(f'month = {month-1} day = {28}')


def elif9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
    if month==2 and day>=29:
        return('0')
    elif month in(1,3,5,7,9,11): 
        if day<31:
            return(f'month = {month} day = {day+1}')
        elif day==31:
            return(f'month = {month+1} day = {1}')
    elif month in(4,6,8,10,12):
        if 1<day<30:
            return(f'month = {month} day = {day+1}')
        elif day==30:
            return(f'month = {month+1} day = {1}')
        elif day>=31:
            return('0')
    elif month==2:   
        if day<28:
            return(f'month = {month} day = {day+1}')
        elif day==28:
            return(f'month = {month+1} day = {1}')


def elif10(symbol, int_namber):
    """
    Elif10. Робот может перемещаться в четырех направлениях («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и принимать три цифровые команды: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_namber - посланная ему команда.
    Вывести направление робота после выполнения полученной команды.
    """
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


def elif11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и может принимать три цифровые команды поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные команды.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    if symbol=='С':
        s=0
    elif symbol=='В':
        s=-1
    elif symbol=='З':
        s=1
    elif symbol=='Ю':
        s=2
    V=s+int1+int2
    if V==0 or V==4:
        return('С')
    elif V==1:
        return('З')
    elif V==-1 or V==3:
        return('В')
    elif V==2 or V==-2:
        return('Ю')
