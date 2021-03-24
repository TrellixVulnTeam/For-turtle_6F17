def elif1(int_namber):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
    if int_number == 1:
        print("понедельник")
    elif int_number == 2:
        print("вторник")
    elif int_number == 3:
        print("среда")
    elif int_number == 4:
        print("четверг")
    elif int_number == 5:
        print("пятница")
    elif int_number == 6:
        print("суббота")
    elif int_number == 7:
        print("воскресенье")


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
    """
    if k == 1:
        print("плохо")
    elif k == 2:
        print("неудовлетворительно")
    elif k == 3:
        print("удовлетворительно")
    elif k == 4:
        print("хорошо")
    elif k == 5:
        print("отлично")
    else:
        print("ошибка")


def elif3(month):
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
    if  3<=month<=5:
        print("весна")
    elif 6<=month<=8:
        print("лето")
    elif 9<=month<=11:
        print("осень")
    elif month==12 or month==1 or month==2:
        print("зима")
    else:
        print("ошибка")    


def elif4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
    if month==2:
        print("28")
    elif month==4 or month==6 or month==9 or month==11:
        print("30")
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print("31")
    else:
        print("ошибка")

def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия n (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    if n==1:
        print(a+b)
    elif n==2:
        print(a-b)
    elif n==3:
        print(a*b)
    elif n==4:
        print(a/b)


def elif6(number, length):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    if number==1:
        print(length*10)
    elif number==2:
        print(length/1000)
    elif number==3:
        print(length)
    elif number==4:
        print(length*1000)
    elif number==5:
        print(length*100)


def elif7(number, mass):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
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

def elif8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
    month("декабрь","январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь")
    if 2<=day<=28:
        print(day-1,"   ",month)
        
    elif day==1 and month==3:
        print(28,"   ",month==2)
        
    elif day==31 and month!=3 and month!=8:
        print(30,"   ",[month-1])
    elif day==30 or (month==8 and day==31):
        print(31,"   ",[month-1])

def elif9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
    month("декабрь","январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь")
    if 1<=day<=27:
        print(day+1,"   ",month)
        
    elif day==31 and month!=2 and month!=7:
        print(30,"   ",[month+1])
        
    elif day==30 or(day==28 and month==2):
        print(30,"   ",[month+1])
    elif day==31 and month!=1 or (month==7 and day==31):
        print(31,"   ",[month+1])

def elif10(symbol, int_namber):
    """
    Elif10. Робот может перемещаться в четырех направлениях«С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и принимать три цифровые команды: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_namber - посланная ему команда.
    Вывести направление робота после выполнения полученной команды.
    """
    if symbol=="С" and int_namber==0:
        print("С")
    elif symbol=="С" and int_namber==1:
        print("З")
    elif symbol=="С" and int_namber==-1:
        print("В")
    elif symbol=="З" and int_namber==0:
        print("З")
    elif symbol=="З" and int_namber==1:
        print("Ю")
    elif symbol=="З" and int_namber==-1:
        print("С")
    elif symbol=="Ю" and int_namber==0:
        print("Ю")
    elif symbol=="Ю" and int_namber==1:
        print("В")
    elif symbol=="Ю" and int_namber==-1:
        print("З")
    elif symbol=="В" and int_namber==0:
        print("В")
    elif symbol=="В" and int_namber==1:
        print("С")
    elif symbol=="В" and int_namber==-1:
        print("Ю")

def elif11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и может принимать три цифровые команды поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные команды.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    if int1==int2==2:
        print(symbol)
    elif (int1==1 and int2==-1) or (int1==-1 and int2==1):
        print(symbol)
        
    elif (int1==int2==1 or int1==int2==-1) and symbol=="С" :
        print("Ю")
    elif (int1==int2==1 or int1==int2==-1) and symbol=="З":
        print("В")
    elif (int1==int2==1 or int1==int2==-1) and symbol=="Ю":
        print("С")
    elif (int1==int2==1 or int1==int2==-1) and symbol=="В":
        print("З")

        
    elif symbol=="С" and ((int1==2 and int2==1) or(int1==1 and int2==2)):
        print("В")
    elif symbol=="З" and ((int1==2 and int2==1) or(int1==1 and int2==2)):
        print("С")
    elif symbol=="Ю" and ((int1==2 and int2==1) or(int1==1 and int2==2)):
        print("З")
    elif symbol=="В" and ((int1==2 and int2==1) or(int1==1 and int2==2)):
        print("Ю")
        
    elif symbol=="С" and ((int1==2 and int2==-1) or(int1==-1 and int2==2)):
        print("З")
    elif symbol=="З" and ((int1==2 and int2==-1) or(int1==-1 and int2==2)):
        print("Ю")
    elif symbol=="Ю" and ((int1==2 and int2==-1) or(int1==-1 and int2==2)):
        print("В")
    elif symbol=="В" and ((int1==2 and int2==-1) or(int1==-1 and int2==2)):
        print("С")