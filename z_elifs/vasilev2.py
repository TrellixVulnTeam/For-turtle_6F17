def elif12(number, element):
    """
    Elif12. Элементы окружности пронумерованы следующим образом:
    1 - радиус r, 2 - диаметр d = 2 * r, 3 - длина l = 2 * pi * r, 4 - площадь круга s = pi * r**2 .
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данной окружности (в том же порядке). В качестве значения π использовать 3.14.
    """
    pi=3.14
    if number in (1,2,3,4):
        if number==1:
            d=element*2
            l=element*2*pi
            s=(element**2)*pi
            return(d,l,s, element)
        elif number==2:
            r=element/2
            l=(element/2)*2*pi
            s=((element/2)**2)*pi
            return(r,l,s, element)
        elif number==3:
            r=element/(2*pi)
            d=(element/(2*pi))*2
            s=((element/(2*pi))**2)*pi
            return(r,d,s, element)
        elif number==4:
            r=(element/pi)**0.5
            d=((element/pi)**0.5)*2
            l=((element/pi)**0.5)*2*pi
            return(r,d,l, element)
    else:
        return('Такой команды 0')


def elif13(number, element):
    """
    Elif13. Элементы равнобедренного прямоугольного треугольника пронумерованы следующим образом:
    1 - катет a, 2 - гипотенуза c = a * 2**0.5, 3 - высота h, опущенная на гипотенузу (h = c / 2),
    4 - площадь s = c * h / 2. Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке).
    """
    if number in (1,2,3,4):
        if number==1:
            c=element*(2**0.5)
            h=(element*(2**0.5))/2
            s=((element*(2**0.5))*((element*(2**0.5))/2))/2
            return(c,h,s, element)
        elif number==2:
            a=element/(2**0.5)
            h=element/2
            s=(element*(element/2))/2
            return(a,h,s,element)
        elif number==3:
            a=(element*2)/(2**0.5)
            c=element*2
            s=((element*2)*element)/2
            return(a,c,s, element)
        elif number==4:
            a=(element*2)**0.5
            c=((element*2)**0.5)*(2**0.5)
            h=(((element*2)**0.5)*(2**0.5))/2
            return(a,c,h, element)
    else:
        return('Такой команды 0')


def elif14(number, element):
    """
    Elif14. Элементы равностороннего треугольника пронумерованы следующим образом:
    1 - сторона a, 2 - радиус r1 вписанной окружности (r1 = a * 3**0.5 / 6),
    3 - радиус r2 описанной окружности (r2 = 2 * r1), 4 - площадь s = a**2 * 3**0.5 / 4.
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке).
    """
    if number in (1,2,3,4):
        if number==1:
            r1=(element*(3**0.5))/6
            r2=2*((element*(3**0.5))/6)
            s=((element**2)*(3**0.5))/4
            return(r1,r2,s, element)
        elif number==2:
            a=element/((3**0.5)*6)
            r2=element*2
            s=(((element/((3**0.5)*6))**2)*(3**0.5))/4
            return(a,r2,s, element)
        elif number==3:
            a=(2/element)/((3**0.5)*6)
            r1=2/element
            s=(((2/element)/((3**0.5)*6)**2)*(3**0.5))/4
            return(a,r1,s, element)
        elif number==4:
            a=(element/((3**0.5)/4))**0.5
            r1=(((element/((3**0.5)/4))**0.5)*(3**0.5))/6
            r2=((((element/((3**0.5)/4))**0.5)*(3**0.5))/6)*2
            return(a,r1,r2,element)
    else:
        return('Такой команды 0')


def elif15(n, m):
    """
    Elif15. Мастям игральных карт присвоены порядковые номера: 1 - пики, 2 - трефы, 3 - бубны, 4 - червы.
    Достоинству карт, старших десятки, присвоены номера: 11 - валет, 12 - дама, 13 - король, 14 - туз.
    Даны два целых числа: num - достоинство (6 ≤ N ≤ 14) и m - масть карты (1 ≤ M ≤ 4).
    Вывести название соответствующей карты вида «шестерка бубен», «дама червей», «туз треф» и т. п.
    """
    if m in (1,2,3,4):
        if 6<=n<=14:
            if m==1:
                if n==6:
                    return('шестерка пики')
                elif n==7:
                    return('семсрка пики')
                elif n==8:
                    return('восьмерка пики')
                elif n==9:
                    return('девятка пики')
                elif n==10:
                    return('десятка пики')
                elif n==11:
                    return('валет пики')
                elif n==12:
                    return('дама пики')
                elif n==13:
                    return('король пики')
                elif n==14:
                    return('туз пики')
            elif m==2:
                if n==6:
                    return('шестерка треф')
                elif n==7:
                    return('семсрка треф')
                elif n==8:
                    return('восьмерка треф')
                elif n==9:
                    return('девятка треф')
                elif n==10:
                    return('десятка треф')
                elif n==11:
                    return('валет треф')
                elif n==12:
                    return('дама треф')
                elif n==13:
                    return('король треф')
                elif n==14:
                    return('туз треф')
            elif m==3:
                if n==6:
                    return('шестерка бубен')
                elif n==7:
                    return('семсрка бубен')
                elif n==8:
                    return('восьмерка бубен')
                elif n==9:
                    return('девятка бубен')
                elif n==10:
                    return('десятка бубен')
                elif n==11:
                    return('валет бубен')
                elif n==12:
                    return('дама бубен')
                elif n==13:
                    return('король бубен')
                elif n==14:
                    return('туз бубен')
            elif m==4:
                if n==6:
                    return('шестерка червей')
                elif n==7:
                    return('семсрка червей')
                elif n==8:
                    return('восьмерка червей')
                elif n==9:
                    return('девятка червей')
                elif n==10:
                    return('десятка червей')
                elif n==11:
                    return('валет червей')
                elif n==12:
                    return('дама червей')
                elif n==13:
                    return('король червей')
                elif n==14:
                    return('туз червей')
        else:
            return('Такого значения нет 0')
    else:
        return('Такой масти нет 0')


def elif16(years_olds):
    """
    Elif16. Дано целое число в диапазоне 20–69, определяющее возраст (в годах).
    Вывести строку-описание указанного возраста, обеспечив правильное согласование числа со словом «год»,
    например: 20 - «двадцать лет», 32 - «тридцать два года», 41 - «сорок один год».
    """
    if 20<=years_olds<=69:
        des=('двадцать','тридцать','сорок','пятьдесят','шестьдесят')
        ed=('лет',
            'один год',
            'два года',
            'три года',
            'четыре года',
            'пять лет',
            'шесть лет',
            'семь лет',
            'восемь лет',
            'девять лет')
        return(des[years_olds//10-2],ed[years_olds%10])
    else:
        return('Неверный возраст')


def elif17(int_number):
    """
    Elif17. Дано целое число в диапазоне 10–40, определяющее количество учебных заданий по некоторой теме.
    Вывести строку-описание указанного количества заданий, обеспечив правильное согласование числа со словами
    «учебное задание», например: 18 - «восемнадцать учебных заданий», 23 - «двадцать три учебных задания»,
    31 - «тридцать одно учебное задание».
   """
    if 10<=int_number<=40:
        if int_number==10:
            return('десять учебных заданий')
        elif 11<=int_number<=19:
            ed=('надцать учебных заданий')
            des=('один','Две','Три',
                 'четыр','Пят','Шест',
                 'сем','восем','Девят')
            return(des[int_number%10-1],ed)
        elif 20<=int_number<=40:
            des=('Двадцать','Тридцать','Сорок','Пятьдесят','Шестьдесят')
            ed=('учебных заданий',
                'одно учебное задание',
                'два учебных задания',
                'три учебных задания',
                'четыре учебных задания',
                'пять учебных заданий',
                'шесть учебных заданий',
                'семь учебных заданий',
                'восемь учебных заданий',
                'девять учебных заданий')
            return(des[int_number//10-2],ed[int_number%10])
    else:
        return('Неверное число')


def elif18(int_number):
    """
    Elif18. Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа,
    например: 256 - «двести пятьдесят шесть», 814 - «восемьсот четырнадцать».
    """
    if 100<=int_number<=999:
        if 11<=int_number%100<=19:
            sot=('Сто','Двести','Триста',
                 'Четыреста','Пятьсот','Шестьсот',
                 'Семьсот','Восемьсот','Девятьсот')
            desed=('одиннадцать','двенадцать',
                   'тринадцать','четырнадцать',
                   'пятнадцать','шестнадцать',
                   'семнадцать','восемнадцать',
                   'девятнадцать')
            return(sot[int_number//100-1],desed[int_number%10-1])
        elif int_number%100==0:
            sot=('Сто','Двести','Триста',
                 'Четыреста','Пятьсот','Шестьсот',
                 'Семьсот','Восемьсот','Девятьсот')
            return(sot[int_number//100-1])
        elif int_number%100//10==0:
            sot=('Сто','Двести','Триста',
                 'Четыреста','Пятьсот','Шестьсот',
                 'Семьсот','Восемьсот','Девятьсот')
            ed=('один','два','три',
                'четыре','пять','шесть',
                'семь','восемь','девять')
            return(sot[int_number//100-1],ed[int_number%10-1])
        elif int_number%10==0:
            sot=('Сто','Двести','Триста',
                 'Четыреста','Пятьсот','Шестьсот',
                 'Семьсот','Восемьсот','Девятьсот')
            des=('десять','двадцать','тридцать',
                 'сорок','пятьдесят','шестьдесят',
                 'семьдесят','восемьдесят','девяносто')
            return(sot[int_number//100-1],des[int_number%100//10-1])
        elif 1<=int_number%10<=9:
            sot=('Сто','Двести','Триста',
                 'Четыреста','Пятьсот','Шестьсот',
                 'Семьсот','Восемьсот','Девятьсот')
            des=('десять','двадцать','тридцать',
                 'сорок','пятьдесят','шестьдесят',
                 'семьдесят','восемьдесят','девяносто')
            ed=('один','два','три',
                'четыре','пять','шесть',
                'семь','восемь','девять')
            return(sot[int_number//100-1],des[int_number%100//10-1],ed[int_number%10-1])
    else:
        return('Неверное число')

def elif19(year):
    """
    Elif19. В восточном календаре принят 60-летний цикл, состоящий из 12-летних под-циклов,
    обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный. В каждом подцикле годы носят
    названия животных: крысы, коровы, тигра, зайца, дракона, змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи.
    По номеру года определить его название, если 1984 год - начало цикла: «год зеленой крысы».
    """
    pass


def elif20(day, month):
    """
    Elif20. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату.
    Вывести знак Зодиака, соответствующий этой дате: «Водолей» (20.1–18.2), «Рыбы» (19.2–20.3), «Овен» (21.3–19.4),
    «Телец» (20.4–20.5), «Близнецы» (21.5–21.6), «Рак» (22.6–22.7), «Лев» (23.7–22.8), «Дева» (23.8–22.9),
    «Весы» (23.9–22.10), «Скорпион» (23.10–22.11), «Стрелец» (23.11–21.12), «Козерог» (22.12–19.1)
    """
    if 1<=month<=2:
        if month==1 and 1<=day<=31:
            if 20<=day<=31:
                return('Водолей')
            else:
                return('Козерог')
        elif month==2 and 1<=day<=29:
            if day<=18:
                return('Водолей')
            else:
                return('Рыбы')
        else:
            return('0 дата')
    elif 3<=month<=4:
        if month==3 and 1<=day<=31:
            if day<=20:
                return('Рыбы')
            else:
                return('Овен')
        elif month==4 and 1<=day<=30:
            if day<=19:
                return('Овен')
            else:
                return('Телец')
        else:
            return('0 дата')
    elif 5<=month<=6:
        if month==5 and 1<=day<=31:
            if day<=20:
                return('Телец')
            else:
                return('Близнецы')
        elif month==6 and 1<=day<=30:
            if day<=21:
                return('Близнецы')
            else:
                return('Рак')
        else:
            return('0 дата')
    elif 7<=month<=8:
        if month==7 and 1<=day<=31:
            if day<=22:
                return('Рак')
            else:
                return('Лев')
        elif month==8 and 1<=day<=31:
            if day<=22:
                return('Лев')
            else:
                return('Дева')
        else:
            return('0 дата')
    elif 9<=month<=10:
        if month==9 and 1<=day<=30:
            if day<=22:
                return('Дева')
            else:
                return('Весы')
        elif month==10 and 1<=day<=31:
            if day<=22:
                return('Весы')
            else:
                return('Скорпион')
        else:
            return('0 дата')
    elif 11<=month<=12:
        if month==11 and 1<=day<=30:
            if day<=22:
                return('Скорпион')
            else:
                return('Стрелец')
        elif month==12 and 1<=day<=31:
            if day<=21:
                return('Стрелец')
            else:
                return('Козерог')
        else:
            return('0 дата')
    else:
        return('0 дата')
