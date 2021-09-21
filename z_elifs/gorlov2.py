def elif12(number, element):
    """
    Elif12. Элементы окружности пронумерованы следующим образом:
    1 - радиус r, 2 - диаметр d = 2 * r, 3 - длина l = 2 * pi * r, 4 - площадь круга s = pi * r**2 .
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данной окружности (в том же порядке). В качестве значения π использовать 3.14.
    """
    π = 3.14
    if number == 1:
        D = element*2
        L = π*D
        S = π*element**2
        return(f'D = {D} L = {L} S = {S}', element)
    elif number == 2:
        r = element/2
        L = 2*π*r
        S = π*r**2
        return(f'r = {r} L = {L} S = {S}', element)
    elif number == 3:
        r = element/(2*π)
        D = 2*r
        S = π*r**2
        return(f'r = {r} D = {D} S = {S}', element)
    elif number == 4:
        r = (element/π)**0.5
        D = 2*r
        L = 2*π*r
        return(f'r = {r} D = {D} L = {L}', element)


def elif13(number, element):
    """
    Elif13. Элементы равнобедренного прямоугольного треугольника пронумерованы следующим образом:
    1 - катет a, 2 - гипотенуза c = a * 2**0.5, 3 - высота h, опущенная на гипотенузу (h = c / 2),
    4 - площадь s = c * h / 2. Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке).
    """
    if number == 1:
        a = element
        c = a*2**0.5
        h = c/2
        S = (c*h)/2
        return(f'c = {c} h = {h} S = {S}')
    elif number == 2:
        c = element
        a = c/2**0.5
        h = c/2
        S = (c*h)/2
        return(f'a = {a} h = {h} S = {S}')
    elif number == 3:
        h = element
        c = h*2
        a = c/2**0.5
        S = (c*h)/2
        return(f'a = {a} c = {c} h = {h} S = {S}')
    elif number == 4:
        S = element
        c = 2*S**0.5
        h = c/2
        a = c/2**0.5
        return(f'a = {a} c = {c} h = {h}')


def elif14(number, element):
    """
    Elif14. Элементы равностороннего треугольника пронумерованы следующим образом:
    1 - сторона a, 2 - радиус r1 вписанной окружности (r1 = a * 3**0.5 / 6),
    3 - радиус r2 описанной окружности (r2 = 2 * r1), 4 - площадь s = a**2 * 3**0.5 / 4.
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке).
    """
    if number == 1:
        a = element
        r1 = a*(3**0.5)/6
        r2 = 2*r1
        S = (a**2)*(3**0.5)/6
        return(f'R1 = {r1} R2 = {r2} S = {S}')
    elif number == 2:
        r1 = element
        a = r1/((3**0.5)/6)
        r2 = 2*r1
        S = (a**2)*(3**0.5)/6
        return(f'a = {a} R2 = {r2} S = {S}')
    elif number == 3:
        r2 = element
        r1 = r2/2
        a = r1/((3**0.5)/6)
        S = (a**2)*(3**0.5)/6
        return(f'a = {a} R1 = {r1} S = {S}')
    elif number == 4:
        S = element
        a = (S/((3**0.5)/6))**0.5
        r1 = a*(3**0.5)/6
        r2 = 2*r1
        return(f'a = {a} R1 = {r1} R2 = {r2} ')


def elif15(n, m):
    """
    Elif15. Мастям игральных карт присвоены порядковые номера: 1 - пики, 2 - трефы, 3 - бубны, 4 - червы.
    Достоинству карт, старших десятки, присвоены номера: 11 - валет, 12 - дама, 13 - король, 14 - туз.
    Даны два целых числа: num - достоинство (6 ≤ N ≤ 14) и m - масть карты (1 ≤ M ≤ 4).
    Вывести название соответствующей карты вида «шестерка бубен», «дама червей», «туз треф» и т. п.
    """
    if 6<=n<=14 and 1<=m<=4:
        if n<11:
            if m==1:
                return(n,'-ка пики',)
            elif m==2:
                return(n,'-ка треф',)
            elif m==3:
                return(n,'-ка бубен',)
            elif m==4:
                return(n,'-ка червей ',)
        elif n==11:
            if m==1:
                return('валет пик')        
            elif m==2:
                return('валет треф')
            elif m==3:
                return('валет бубен')
            elif m==4:
                return('валет червей ')
        elif n==12:
            if m==1:
                return('дама пик')        
            elif m==2:
                return('дама треф')
            elif m==3:
                return('дама бубен')
            elif m==4:
                return('дама червей ')
        elif n==13:
            if m==1:
                return('король пик')        
            elif m==2:
                return('король треф')
            elif m==3:
                return('король бубен')
            elif m==4:
                return('король червей ')
        elif n==14:
            if m==1:
                return('туз пик')        
            elif m==2:
                return('туз треф')
            elif m==3:
                return('туз бубен')
            elif m==4:
                return('туз червей ')
    else:
        return('такой карты не существует')


def elif16(years_olds):
    """
    Elif16. Дано целое число в диапазоне 20–69, определяющее возраст (в годах).
    Вывести строку-описание указанного возраста, обеспечив правильное согласование числа со словом «год»,
    например: 20 - «двадцать лет», 32 - «тридцать два года», 41 - «сорок один год».
    """
    n = years_olds%10
    N = (years_olds-n)/10
    if N==2:
        Q = 'двадцать'
    elif N==3:
        Q = 'тридцать'
    elif N==4:
        Q = 'сорок'
    elif N==5:
        Q = 'пятьдесят'
    elif N==6:
        Q = 'шестьдесят'
    if n==1:
        q = 'один год'
    elif n==2:
        q = 'два года'
    elif n==3:
        q = 'три года'
    elif n==4:
        q = 'четыре года'
    elif n==5:
        q = 'пять лет'
    elif n==6:
        q = 'шесть лет'
    elif n==7:
        q = 'семь лет'
    elif n==8:
        q = 'восемь лет'
    elif n==9:
        q = 'девять лет'
    elif n==0:
        q = 'лет'
    return(Q,q)


def elif17(int_number):
    """
    Elif17. Дано целое число в диапазоне 10–40, определяющее количество учебных заданий по некоторой теме.
    Вывести строку-описание указанного количества заданий, обеспечив правильное согласование числа со словами
    «учебное задание», например: 18 - «восемнадцать учебных заданий», 23 - «двадцать три учебных задания»,
    31 - «тридцать одно учебное задание».
   """
    n = int_number%10
    N = (int_number-n)/10
    if int_number==10:
        Q = 'десять'
    elif int_number==11:
        Q = 'одинадцать'
    elif int_number==12:
        Q = 'двенадцать'
    elif int_number==13:
        Q = 'тринадцать'
    elif int_number==14:
        Q = 'четырнадцать'
    elif int_number==15:
        Q = 'пятнадцать'
    elif int_number==16:
        Q = 'шестнадцать'
    elif int_number==17:
        Q = 'семнадцать'
    elif int_number==18:
        Q = 'восемнадцать'
    elif int_number==19:
        Q = 'девятнадцать'
    elif N==2:
        Q = 'двадцать'
    elif N==3:
        Q = 'тридцать'
    elif N==4:
        Q = 'сорок'
    if int_number>19 and n==1:
        q = 'одно учебное задание'
    elif int_number>19 and n==2:
        q = 'два учебных задания'
    elif int_number>19 and n==3:
        q = 'три учебных задания'
    elif int_number>19 and n==4:
        q = 'четыре учебных задания'
    elif int_number>19 and n==5:
        q = 'пять учебных заданий'
    elif int_number>19 and n==6:
        q = 'шесть учебных заданий'
    elif int_number>19 and n==7:
        q = 'семь учебных заданий'
    elif int_number>19 and n==8:
        q = 'восемь учебных заданий'
    elif int_number>19 and n==9:
        q = 'девять учебных заданий'
    else:
        q = 'учебных заданий'
    return(Q,q)


def elif18(int_number):
    """
    Elif18. Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа,
    например: 256 - «двести пятьдесят шесть», 814 - «восемьсот четырнадцать».
    """
    a= ("сто","двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот")
    b= ("десять","одинадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать")
    с= ("двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто")
    d= ("один","два","три","четыре","пять","шесть","семь","восемь","девять","")

    n = int_number%10
    N = int_number%100//10
    W = int_number//100

    if  1<=W<=9:
        if N==0:
            return(a[W-1],d[n-1])
        elif N==1:
            return(a[W-1],b[n-1])
        elif 2<=N<=9:
            return(a[W-1],с[N-2], d[n-1])

def elif19(year):
    """
    Elif19. В восточном календаре принят 60-летний цикл, состоящий из 12-летних под-циклов,
    обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный. В каждом подцикле годы носят
    названия животных: крысы, коровы, тигра, зайца, дракона, змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи.
    По номеру года определить его название, если 1984 год - начало цикла: «год зеленой крысы».
    """
    n = (abs(year-1894))%12
    N = (abs(year-1894))%60//12
    c1=("зеленого", "красного", "желтого", "белого", "черного")
    c2=("зеленой", "красной", "желтой", "белой", "черной")
    animal=("крысы","коровы","тигра","зайца","дракона","змеи","лошади","овцы","обезьяны","курицы","собаки","свиньи")

    if n-1==2 or n-1==3:
        return('год',c1[N],animal[n])
    else:
        return('год',c2[N],animal[n])


def elif20(day, month):
    """
    Elif20. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату.
    Вывести знак Зодиака, соответствующий этой дате: «Водолей» (20.1–18.2), «Рыбы» (19.2–20.3), «Овен» (21.3–19.4),
    «Телец» (20.4–20.5), «Близнецы» (21.5–21.6), «Рак» (22.6–22.7), «Лев» (23.7–22.8), «Дева» (23.8–22.9),
    «Весы» (23.9–22.10), «Скорпион» (23.10–22.11), «Стрелец» (23.11–21.12), «Козерог» (22.12–19.1)
    """
    def qwadrat (month,day):
        k = 0
        if month in (1,3,5,7,8,10,12) and 1<=day<=31:
            month*=100
            k=month+day
            return k
        elif month in (4,6,9,11) and 1<=day<=30:
            month*=100
            k=month+day
            return k
        elif month==2 and 1<=day<=29:
            month*=100
            k=month+day
            return k
        else:
            return 0
        
    q=month
    w=day

    if 201<=qwadrat(q,w)<=218:
        return('водолей')
    elif 219<=qwadrat(q,w)<=320:
        return('рыбы')
    elif 321<=qwadrat(q,w)<=419:
        return('овен')
    elif 420<=qwadrat(q,w)<=520:
        return('телец')
    elif 521<=qwadrat(q,w)<=621:
        return('близнецы')
    elif 622<=qwadrat(q,w)<=722:
        return('рак')
    elif 723<=qwadrat(q,w)<=822:
        return('лев')
    elif 823<=qwadrat(q,w)<=922:
        return('дева')
    elif 923<=qwadrat(q,w)<=1022:
        return('весы')
    elif 1023<=qwadrat(q,w)<=1122:
        return('скорпион')
    elif 1123<=qwadrat(q,w)<=1221:
        return('стрелец')
    elif 1222<=qwadrat(q,w)<=1231 or 0<=qwadrat(q,w)<=191 :
        return('козерог')
    else:
        return('нет такой даты')
