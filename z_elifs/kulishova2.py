def elif12(number, element):
    """
    Elif12. Элементы окружности пронумерованы следующим образом:
    1 - радиус r, 2 - диаметр d = 2 * r, 3 - длина l = 2 * pi * r, 4 - площадь круга s = pi * r**2 .
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данной окружности (в том же порядке). В качестве значения π использовать 3.14.
    """
    p=3.14
    if number==1:
        d=2*element
        l=2*p*element
        s=p*element**2
        return(d, l, s, element)
    elif number==2:
        r=element/2
        l=2*p*r
        s=p*r**2
        return(r, l, s, element)
    elif number==3:
        d=element/p
        r=d/2
        s=p*r**2
        return(d, r, s, element)
    elif number==4:
        r=(element/p)**0.5
        d=2*r
        l=p*d
        return(d, l, r, element)
    else:
        return(0)


def elif13(number, element):
    """
    Elif13. Элементы равнобедренного прямоугольного треугольника пронумерованы следующим образом:
    1 - катет a, 2 - гипотенуза c = a * 2**0.5, 3 - высота h, опущенная на гипотенузу (h = c / 2),
    4 - площадь s = c * h / 2. Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке).
    """
    if number==1:
        c=element*(2**0.5)
        h=c/2
        S=c*h/2
        return('c=',c, 'h=',h, 'S=',S, element)
    elif number==2:
        a=element/(2**0.5)
        h=element/2
        S=element*h/2
        return('c=',a, 'h=',h, 'S=',S, element)
    elif number==3:
        a=element*(2**0.5)
        c=a**(2**0.5)
        S=c*element/2
        return('c=',c, 'h=',a, 'S=',S, element)
    elif number==4:
        a=(2*element)**0.5
        c=a*(2**0.5)
        h=c/2
        return('c=',c, 'h=',h, 'S=',a, element)
    else:
        return('Ошибка')


def elif14(number, element):
    """
    Elif14. Элементы равностороннего треугольника пронумерованы следующим образом:
    1 - сторона a, 2 - радиус r1 вписанной окружности (r1 = a * 3**0.5 / 6),
    3 - радиус r2 описанной окружности (r2 = 2 * r1), 4 - площадь s = a**2 * 3**0.5 / 4.
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке).
    """
    if number==1:
        R1=element*3**0.5/6
        R2=2*R1
        S=element*element*3**0.5/4
        return('R1=',R1)
        return('R2=',R2)
        return('S=',S)
    elif number==2:
        a=2*(3**0.5)*element
        R2=2*element
        S=a*a*(3**0.5)/4
        return('a=',a)
        return('R2=',R2)
        return('S=',S)
    elif number==3:
        R1=element/2
        a=2*3**0.5*R1
        S=a*a*3**0.5/4
        return('a=',a)
        return('R1=',R1)
        return('S=',S)
    elif number==4:
        a=2*(element/3**0.5)**0.5
        R1=element*3**0.5/6
        R2=2*R1
        return('a=',a)
        return('R1=',R1)
        return('R2=',R2)
    else:
        return('Ошибка')


def elif15(n, m):
    """
    Elif15. Мастям игральных карт присвоены порядковые номера: 1 - пики, 2 - трефы, 3 - бубны, 4 - червы.
    Достоинству карт, старших десятки, присвоены номера: 11 - валет, 12 - дама, 13 - король, 14 - туз.
    Даны два целых числа: num - достоинство (6 ≤ N ≤ 14) и m - масть карты (1 ≤ M ≤ 4).
    Вывести название соответствующей карты вида «шестерка бубен», «дама червей», «туз треф» и т. п.
    """
    if n==6:
        Str='Шестерка'
    elif n==7:
        Str='Семерка'
    elif n==8:
        Str='Восьмерка'
    elif n==9:
        Str='Девятка'
    elif n==10:
        Str='Десятка'
    elif n==11:
        Str='Валет'
    elif n==12:
        Str='Дама'
    elif n==13:
        Str='Король'
    elif n==14:
        Str='Туз'
    else:
        n==-1
    
    if n!=-1:
        if m==1:
            return(Str,' пики')
        elif m==2:
            return(Str,' треф')
        elif m==3:
            return(Str,' бубен')
        elif m==4:
            return(Str,' червей')
        else:
            return('Ошибка')
    else:
        return('Ошибка')


def elif16(years_olds):
    """
    Elif16. Дано целое число в диапазоне 20–69, определяющее возраст (в годах).
    Вывести строку-описание указанного возраста, обеспечив правильное согласование числа со словом «год»,
    например: 20 - «двадцать лет», 32 - «тридцать два года», 41 - «сорок один год».
    """
    x=years_olds%10
    y=years_olds//10
    
    if y==2:
        years_olds_str='Двадцать'
    elif y==3:
        years_olds_str='Тридцать'
    elif y==4:
        years_olds_str='Сорок'
    elif y==5:
        years_olds_str='Пятьдесят'
    elif y==6:
        years_olds_str='Шестдесят'
    else:
        x=-1
        
    if x==0:
        return(years_olds_str,'лет')
    elif x==1:
        return(years_olds_str,'один год')
    elif x==2:
        return(years_olds_str,'два года')
    elif x==3:
        return(years_olds_str,'три года')
    elif x==4:
        return(years_olds_str,'четыре года')
    elif x==5:
        return(years_olds_str,'пять лет')
    elif x==6:
        return(years_olds_str,'шесть лет')
    elif x==7:
        return(years_olds_str,'семь лет')
    elif x==8:
        return(years_olds_str,'восемь лет')
    elif x==9:
        return(years_olds_str,' девять лет')
    elif x==-1:
        return('Введено не 0 0')


def elif17(int_number):
    """
    Elif17. Дано целое число в диапазоне 10–40, определяющее количество учебных заданий по некоторой теме.
    Вывести строку-описание указанного количества заданий, обеспечив правильное согласование числа со словами
    «учебное задание», например: 18 - «восемнадцать учебных заданий», 23 - «двадцать три учебных задания»,
    31 - «тридцать одно учебное задание».
   """
    if 10<=int_number<=40:
        #Проверила на промежуток от 11 до 19
        if int_number==11:
            Str='Одинадцать'
        elif int_number==12:
            Str='Двенадцать'
        elif int_number==13:
            Str='Тринадцать'
        elif int_number==14:
            Str='Четырнадцать'
        elif int_number==15:
            Str='Пятнадцать'
        elif int_number==16:
            Str='Шестнадцать'
        elif int_number==17:
            Str='Семнадцать'
        elif int_number==18:
            Str='Восемнадцать'
        elif int_number==19:
            Str='Девятнадцать'
        else:
            #Иначе вычеслила десятки
            if int_number//10==1:
                Str='Десять'
            elif int_number//10==2:
                Str='Двадцать'
            elif int_number//10==3:
                Str='Тридцать'
            elif int_number//10==4:
                Str='Сорок'
            #Вычеслила единицы
            x=int_number%10
            if x==1:
                Str+=' одно'
            elif x==2:
                Str+=' два'
            elif x==3:
                Str+=' три'
            elif x==4:
                Str+=' четыре'
            elif x==5:
                Str+=' пять'
            elif x==6:
                Str+=' шесть'
            elif x==7:
                Str+=' семь'
            elif x==8:
                Str+=' восемь'
            elif x==9:
                Str+=' девять'
        #Добавила окончание
        if 10<=int_number<=20 or 25<=int_number<=30 or 35<=int_number<=40:
            Str+=' учебных заданий'
        elif int_number in [22,23,24,32,33,34]:
            Str+=' учебных задания'
        elif int_number==21 or int_number==31:
            Str+=' учебное задание'
        
        return(Str)
    else:
        return('Ошибка')


def elif18(int_number):
    """
    Elif18. Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа,
    например: 256 - «двести пятьдесят шесть», 814 - «восемьсот четырнадцать».
    """
    X=int_number//100

    Y=int_number//10%10

    Z=int_number%10

    
    if X==1:
        Str='Сто'
    elif X==2:
        Str='Двести'
    elif X==3:
        Str='Триста'
    elif X==4:
        Str='Четыреста'
    elif X==5:
        Str='Пятьсот'
    elif X==6:
        Str='Шестьсот'
    elif X==7:
        Str='Семьсот'
    elif X==8:
        Str='Восемьсот'
    elif X==9:
        Str='Девятьсот'
    else:
        int_number=0
    
    if int_number!=0:
        #Создала десятки
        if Y==2:
            Str+=' двадцать'
        elif Y==3:
            Str+=' тридцать'
        elif Y==4:
            Str+=' сорок'
        elif Y==5:
            Str+=' пятьдесят'
        elif Y==6:
            Str+=' шестьдесят'
        elif Y==7:
            Str+=' семьдесят'
        elif Y==8:
            Str+=' восемьдесят'
        elif Y==9:
            Str+=' девяносто'
        #Созадала единицы
             #Если десяток начинается на единицу
        if Y==1: 
            if Z==0:
                Str+=' десять'
            elif Z==1:
                Str+=' одинадцать'
            elif Z==2:
                Str+=' двенадцать'
            elif Z==3:
                Str+=' тринадцать'
            elif Z==4:
                Str+=' четырнадцать'
            elif Z==5:
                Str+=' пятнадцать'
            elif Z==6:
                Str+=' шестнадцать'
            elif Z==7:
                Str+=' семнадцать'
            elif Z==8:
                Str+=' восемнадцать'
            elif Z==9:
                Str+=' девятнадцать'
        else:
            if Z==1:
                Str+=' один'
            elif Z==2:
                Str+=' два'
            elif Z==3:
                Str+=' три'
            elif Z==4:
                Str+=' четыре'
            elif Z==5:
                Str+=' пять'
            elif Z==6:
                Str+=' шесть'
            elif Z==7:
                Str+=' семь'
            elif Z==8:
                Str+=' восемь'
            elif Z==9:
                Str+=' девять'
        return(Str)
    else:
        return('0 ввода')

def elif19(year):
    """
    Elif19. В восточном календаре принят 60-летний цикл, состоящий из 12-летних под-циклов,
    обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный. В каждом подцикле годы носят
    названия животных: крысы, коровы, тигра, зайца, дракона, змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи.
    По номеру года определить его название, если 1984 год - начало цикла: «год зеленой крысы».
    """
    Str='Год '
    if year>1983:
        year=(year-1984)%60+1
    else:
        year=61-(1984-year)%60
    
    Cl=(year-1)%10+1
    Cl=(Cl-1)//2+1
    if Cl==1:
        Str+='зелено'
    elif Cl==2:
        Str+='красно'
    elif Cl==3:
        Str+='желто'
    elif Cl==4:
        Str+='бело'
    elif Cl==5:
        Str+='черно'
    
    A=(year)%12
    if A in [3,4,5]:
        Str+='го'
    else:
        Str+='й'
    
    if A==1:
        Str+=' крысы'
    elif A==2:
        Str+=' коровы'
    elif A==3:
        Str+=' тигра'
    elif A==4:
        Str+=' зайца'
    elif A==5:
        Str+=' дракона'
    elif A==6:
        Str+=' змеи'
    elif A==7:
        Str+=' лощади'
    elif A==8:
        Str+=' овцы'
    elif A==9:
        Str+=' обезьяны'
    elif A==10:
        Str+=' курицы'
    elif A==11:
        Str+=' собаки'
    elif A==12:
        Str+=' свиньи'
    
    return(Str)


def elif20(day, month):
    """
    Elif20. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату.
    Вывести знак Зодиака, соответствующий этой дате: «Водолей» (20.1–18.2), «Рыбы» (19.2–20.3), «Овен» (21.3–19.4),
    «Телец» (20.4–20.5), «Близнецы» (21.5–21.6), «Рак» (22.6–22.7), «Лев» (23.7–22.8), «Дева» (23.8–22.9),
    «Весы» (23.9–22.10), «Скорпион» (23.10–22.11), «Стрелец» (23.11–21.12), «Козерог» (22.12–19.1)
    """
    if month==1:
        if day>20:
            return('Водолей')
        else:
            return('Козерог')
    elif month==2:
        if day<19:
            return('Водолей')
        else:
            return('Рыбы')
    elif month==3:
        if day<21:
            return('Рыбы')
        else:
            return('Овен')
    elif month==4:
        if day<20:
            return('Овен')
        else:
            return('Телец')
    elif month==5:
        if day<21:
            return('Телец')
        else:
            return('Близнецы')
    elif month==6:
        if day<22:
            return('Близнецы')
        else:
            return('Рак')
    elif month==7:
        if day<23:
            return('Рак')
        else:
            return('Лев')
    elif month==8:
        if day<23:
            return('Лев')
        else:
            return('Дева')
    elif month==9:
        if day>23:
            return('Дева')
        else:
            return('Весы')
    elif month==10:
        if day<23:
            return('Весы')
        else:
            return('Скорпион')
    elif month==11:
        if day<23:
            return('Скорпион')
        else:
            return('Стрелец')
    elif month==12:
        if day<22:
            return('Стрелец')
        else:
            return('Козерог')
