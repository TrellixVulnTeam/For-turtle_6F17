def elif1(int_namber):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.).
    """
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


def elif2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если K не лежит в диапазоне 1–5, то вывести строку «0».
    """
    if (1>k) or (k>5):
        return('0')
    elif k==1:
        return('плохо')
    elif k==2:
        return('неудовлетворительно')
    elif k==3:
        return('удовлетворительно')
    elif k==4:
        return('хорошо')
    elif k==5:
        return('отлично')


def elif3(month):
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
    if (1>month) or (month>12):
        return('0')
    elif month==12 or 1<=month<=2:
        return('зима')
    elif 3<=month<=5:
        return('весна')
    elif 6<=month<=8:
        return('лето')
    elif 9<=month<=11:
        return('осень')


def elif4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
    if (month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12):
        return('Количество дней в этом месяце: 31')
    elif(month==2):
        return('Количество дней в этом месяце: 28')
    elif (month==4) or (month==6) or (month==11) or (month==9):
        return('Количество дней в этом месяце: 30')
    else:
        return('0')


def elif5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия num (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    if n==1:
        return(f'{a}+{b}={a+b}')
    elif n==2:
        return(f'{a}-{b}={a-b}')
    elif n==3:
        return(f'{a}*{b}={a*b}')
    elif n==4 and b==0:
        return('На ноль делить нельзя')
    elif n==4:
        return(f'{a}/{b}={a/b}')
    elif n>4 or n<1:
        return('Не верно введено num')
    
        


def elif6(number, length):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - кило-метр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    if number==1:
        return(f'{length} дециметр = {length*.1} метр')
    elif number==2:
        return(f'{length} километр = {length*1000} метр')
    elif number==3:
        return(f'{length} метр = {length} метр')
    elif number==4:
        return(f'{length} миллиметр = {length*0.001} метр')
    elif number==5:
        return(f'{length} сантиметр = {length*0.01} метр')
    elif number>5 or number<1:
        return('Не верно введено number')


def elif7(number, mass):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - милли-грамм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
    if number==1:
        return(f'{mass} килограмм ={mass} килограмм')
    elif number==2:
        return(f'{mass} милли-грамм ={mass*0.000001} килограмм')
    elif number==3:
        return(f'{mass} грамм ={mass*0.001} килограмм')
    elif number==4:
        return(f'{mass} тонна ={mass*1000} килограмм')
    elif number==5:
        return(f'{mass} центнер ={mass*100} килограмм')
    elif number>5 or number<1:
        return('Не верно введено number')


def elif8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
    if (month==1) and (day==1):
        day=31
        month=12
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==1) and (1<day<=31):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==2) and (day==1):
        day=31
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==2) and (1<day<=28):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==3) and (day==1):
        day=28
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==3) and (1<day<=31):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==4) and (day==1):
        day=31
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==4) and (1<day<=30):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==5) and (day==1):
        day=30
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==5) and (1<day<=31):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==6) and (day==1):
        day=31
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==6) and (1<day<=30):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==7) and (day==1):
        day=30
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==7) and (1<day<=31):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==8) and (day==1):
        day=31
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==8) and (1<day<=31):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==9) and (day==1):
        day=31
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==9) and (1<day<=30):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==10) and (day==1):
        day=30
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==10) and (1<day<=31):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==11) and (day==1):
        day=31
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==11) and (1<day<=30):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==12) and (day==1):
        day=30
        month-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    elif (month==12) and (1<day<=31):
        day-=1
        return(f'Предыдущая дата: месяц: {month} день: {day}')
    else:
        return('0')
    
    
            
            


def elif9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
    if (month==1) and (day==31):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==1) and (1<=day<31):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==2) and (day==28):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==2) and (1<=day<28):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==3) and (day==31):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==3) and (1<=day<31):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==4) and (day==30):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==4) and (1<=day<30):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==5) and (day==31):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==5) and (1<=day<31):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==6) and (day==30):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==6) and (1<=day<30):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==7) and (day==31):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==7) and (1<=day<31):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==8) and (day==31):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==8) and (1<=day<31):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==9) and (day==30):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==9) and (1<=day<30):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==10) and (day==31):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==10) and (1<=day<31):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==11) and (day==30):
        day=1
        month+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==11) and (1<=day<30):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==12) and (day==31):
        day=1
        month=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    elif (month==12) and (1<=day<31):
        day+=1
        return(f'Следующая дата: месяц: {month} день: {day}')
    else:
        return('0')


def elif10(symbol, int_namber):
    """
    Elif10. Робот может перемещаться в четырех направлениях («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и принимать три цифровые команды: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_namber - посланная ему команда.
    Вывести направление робота после выполнения полученной команды.
    """
    flag = True
    while flag:
        if (symbol=="С" or symbol=="З" or symbol=="Ю" or symbol=="В") and (int_namber==0 or int_namber==-1 or int_namber==1):
            flag=False
        else:
            return("Пока что переменные не введениы, либо они введены неправильно")
    if symbol=='С':
        if int_namber==0:
            symbol='Севера'
        elif int_namber==-1:
            symbol='Востока'
        elif int_namber==1:
            symbol='Запада'
        else:
            return('Неверно введена команда')
    if symbol=='З':
        if int_namber==-1:
            symbol='Севера'
        elif int_namber==1:
            symbol='Юга'
        elif int_namber==0:
            symbol='Запада'
        else:
            return('Неверно введена команда')
    if symbol=='Ю':
        if int_namber==1:
            symbol='Восток'
        elif int_namber==0:
            symbol='Юга'
        elif int_namber==-1:
            symbol='Запада'
        else:
            return('Неверно введена команда')
    if symbol=='В':
        if int_namber==0:
            symbol='Восток'
        elif int_namber==-1:
            symbol='Юга'
        elif int_namber==1:
            symbol='Север'
    return(f'Робот направлен в сторону {symbol}')
    
        


def elif11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и может принимать три цифровые команды поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные команды.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    flag = True
    while flag:
         if (symbol=="С" or symbol=="З" or symbol=="Ю" or symbol=="В") and (int1==2 or int1==-1 or int1==1) and (int2==2 or int2==-1 or int2==1):
            flag=False
         else:
            return("Пока что переменные не введениы, либо они введены неправильно")
    if ((int1+int2)==0) or ((int1+int2)==4):
        int_namber=0
    elif (int1+int2)==3:
        int_namber=-1
    elif (int1+int2)==1:
        int_namber=1
    elif ((int1+int2)==2 or (int1+int2)==-2) :
        int_namber=2
    else:
        pass

    if symbol=='С':
        if int_namber==0:
            symbol='Севера'
        elif int_namber==-1:
            symbol='Востока'
        elif int_namber==1:
            symbol='Запада'
        else:
            symbol='Юга'
    if symbol=='З':
        if int_namber==-1:
            symbol='Севера'
        elif int_namber==1:
            symbol='Юга'
        elif int_namber==0:
            symbol='Запада'
        else:
            symbol='Восток'
    if symbol=='Ю':
        if int_namber==1:
            symbol='Восток'
        elif int_namber==0:
            symbol='Юга'
        elif int_namber==-1:
            symbol='Запада'
        else:
            symbol='Севера'
    if symbol=='В':
        if int_namber==0:
            symbol='Восток'
        elif int_namber==-1:
            symbol='Юга'
        elif int_namber==1:
            symbol='Север'
        else:
            symbol='Запада'
    return(f'Робот направлен в сторону {symbol}')
#elif1(8)
#elif2(6)
#elif3(13)
#elif4(13)
#elif5(0, 4, 0)
#elif6(0, 100)
#elif7(0, 1)
#elif8(31,1)
#elif9(31,2)
#elif10("В", 1)
#elif11("", -1, 2)
