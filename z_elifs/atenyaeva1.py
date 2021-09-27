def elif1(int_namber):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
def elif1(int_namber):
    if int_namber==1:
        return("понедельник")
    elif int_namber==2:
        return("вторник")
    elif int_namber==3:
        return("среда")
    elif int_namber==4:
        return("четверг")
    elif int_namber==5:
        return("пятница")
    elif int_namber==6:
        return("суббота")
    elif int_namber==7:
        return("воскресенье")
    else:
        return("нет такого дня")
  


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
    """
def elif2(k):
    if k==1:
        return("плохо")
    elif k==2:
        return("неудовлетворительно")
    elif k==3:
        return("удовлетворительно")
    elif k==4:
        return("хорошо")
    elif k==5:
        return("отлично")
    else:
        return("ошибка")
 


def elif3(month):
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
def elif3(month):
    if month==1 or month==2 or month==12:
        return("зима")
    elif month==3 or month==3 or month==5:
        return("весна")
    elif month==6 or month==7 or month==8:
        return("лето")
    elif month==9 or month==10 or month==11:
        return("оcень")
    else:
        return("0 не подходит")

def elif4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
def elif4(month):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return("31")
    elif  month==4 or month==6 or month==9 or month==11:
        return("30")
    elif month==2:
        return("28")
    else:
        return("нет такого числа")


def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия num (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
def elif5(n, a, b):
    if n==1:
        return(a+b)
    elif n==2 :
        return(a-b)
    elif n==3:
        return(a*b)
    elif n==4:
        return(a/b)
    else:
        return("нет такого числа") 
 


def elif6(number, length):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
def elif6(number, length):
    if number==1:
        return(length/10)
    elif number==2 :
        return(length*1000)
    elif number==3:
        return(length)
    elif number==4:
        return(length/1000)
    elif number==5:
        return(length/100)    
    else:
        return("число не подходит") 




def elif7(number, mass):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
def elif7(number, mass):
    if number==1:
        return(mass)
    elif number==2 :
        return(mass/1000000)
    elif number==3:
        return(mass/1000)
    elif number==4:
        return(mass*1000)
    elif number==5:
        return(mass*100)    
    else:
        return("число не подходит")


def elif8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
def elif8(day, month):
    day=day-1
    if day==0:
        month=month-1
    if month in (1,3,5,7,8,10) and day>31:
        day=1
        month=month-1
    elif month in (4,6,9,11) and day>30:
        day=1
        month=month-1
    elif month==12 and day>31:
        day=1
        month=1
    elif month==2 and day>28:
        day=1
        month=month-1
    if day==0 and month in (1,3,5,7,8,10,12):
        day=31
    elif day==0 and month in (4,6,9,11):
        day=30
    elif day==0 and month==2:
        day=28
    return(day, month)
    


def elif9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
def elif9(day, month):
    day=day+1
    if month in (1,3,5,7,8,10) and day>31:
        day=1
        month=month+1
    elif month in (4,6,9,11) and day>30:
        day=1
        month=month+1
    elif month==12 and day>31:
        day=1
        month=1
    elif month==2 and day>28:
        day=1
        month=month+1
    return(day,month)        
    


def elif10(symbol, int_namber):
    """
    Elif10. Робот может перемещаться в четырех направлениях («С» - С, «З» - З, «Ю» - Ю, «В» - В)
    и принимать три цифровые команды: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_namber - посланная ему команда.
    Вывести направление робота после выполнения полученной команды.
    """
def elif10(symbol:str, int_namber):
    if symbol=="С":
            if int_namber==1:
                return("З")
            elif int_namber==0:
                return("С")
            elif  int_namber==-1:
                return("В")
    elif symbol=="В":
            if int_namber==1:
                return("С")
            elif int_namber==0:
                return("В")
            elif  int_namber==-1:
                return("Ю")
    elif symbol=="Ю":
            if int_namber==1:
                return("В")
            elif int_namber==0:
                return("Ю")
            elif  int_namber==-1:
                return("З")
    elif symbol=="З":
            if int_namber==1:
                return("Ю")
            elif int_namber==0:
                return("З")
            elif  int_namber==-1:
                return("С") 


def elif11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - С, «З» - З, «Ю» - Ю, «В» - В)
    и может принимать три цифровые команды поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные команды.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    pass