def elif12(number, element):
    p=3.14
    if element==1:
        d1=2*number
        l1=2*p*number
        s1=p*(number**2)
        print('D - ',d1,'L - ','{:2.3f}'.format(l1),'S - ',s1)
    elif element==2:
        r1=number/2
        l1=2*p*r1
        s1=p*(r1**2)
        print('R - ','{:2.3f}'.format(r1),'L - ','{:2.3f}'.format(l1),'S - ','{:2.3f}'.format(s1))
    elif element==3:
        r1=number/2*p
        d1=2*r1
        s1=p*(r1**2)
        print('D -','{:2.3f}'.format(d1),'R - ','{:2.3f}'.format(r1),'S - ','{:2.3f}'.format(s1))
    elif element==4:
        r1=(number/p)**0.5
        d1=2*r1
        l1=2*p*r1
        print('D - ','{:2.3f}'.format(d1),'L -','{:2.3f}'.format(l1),'R - ','{:2.3f}'.format(r1))
    elif 1<=element<=4 and number<0:
        print('Неправильный ввод числа')
        
        
def elif13(number, element):
    if element==1:
        c=number*((2)**0.5)
        h=c/2
        s=c*(h/2)
        print('C- ','{:2.3f}'.format(c),'h - ','{:2.3f}'.format(h),'s -','{:2.3f}'.format(s))
    elif element==2:
        a=number/(2**0.5)
        h=number/2
        s=number*(h/2)
        print('A - ','{:2.3f}'.format(a),'h - ','{:2.3f}'.format(h),'S -','{:2.3f}'.format(s))
    elif element==3:
        c=number*2
        s=c*h/2
        a=c/(2**0.5)
        print('A - ','{:2.3f}'.format(a),'S - ','{:2.3f}'.format(s),'C -','{:2.3f}'.format(c))
    elif element==4:
        c=number/4
        h=c/2
        a=c/(2**0.5)
        print('A - ','{:2.3f}'.format(a),'h - ','{:2.3f}'.format(h),'C -','{:2.3f}'.format(c))

def elif14(number, element):
    if element==1:
        r1=number* (3**0.5)/6
        r2=r1*2
        s=(number**2) * (3**0.5) / 4
        print('R1 - ',r1,'R2 - ',r2,'S - ',s)
    elif element==2:
        a=number*6/3(**0.5)
        r2=2*number
        s=(a**2)*(3**0.5)/4
        print('A - ',a,'R2 - ',r2,'S - ',s)
    elif element==3:
        r1=number/2
        a=r1*6/3(**0.5)
        s=(a**2)*(3**0.5)/4
        print('R1 - ',r1,'A - ',a,'S - ',s)
    elif element==4:
        a=(number*4/(3**0.5))**0.5
        r1=a*(3**0.5)/6
        r2=r1*2
        print('A - ',a,'R1 - ',r1,'R2 - ',r2)
    elif 1<element<4 and number<0:
        print('Неправильный ввод числа')


def elif15(n, m):
    if m==1:
        m='пики'
    elif m==2:
        m='Трефы'
    elif m==3:
        m='бубны'
    elif m==4:
        m='черви'
    else:
        m='Ошибка'       
    if n==6:
        n='Шестерка'
    elif n==7:
        n='Семерка'
    elif n==8:
        n='Восьмерка'
    elif n==9:
        n='Девятка'
    elif n==10:
        n='Десятка'
    elif n==11:
        n='Валет'
    elif n==12:
        n='Дама'
    elif n==13:
        n='Король'
    elif n==14:
        n='Туз'
    else:
        n='Ошибка'
    print(n,m)
    

def elif16(years_old):
    if 20<=years_old<=69:
        if (years_old%10==1) and (years_old!=11):
            m='год'
        elif (years_old%10>1) and (years_old%10<5) and (years_old!=12) and (years_old!=13) and (years_old!=14):
            m='года'
        else:
            m='лет'
        if years_old//10==2:
            a='двадцать'
        elif years_old//10==3:
            a='тридцать'
        elif years_old//10==4:
            a='сорок'
        elif years_old//10==5:
            a='пятьдесят'
        elif years_old//10==6:
            a='шестьдесят'
        if years_old%10==1:
            b='один'
        elif years_old%10==2:
            b='два'
        elif years_old%10==3:
            b='три'
        elif years_old%10==4:
            b='четыре'
        elif years_old%10==5:
            b='пять'
        elif years_old%10==6:
            b='шесть'
        elif years_old%10==7:
            b='семь'
        elif years_old%10==8:
            b='восемь'
        elif years_old%10==9:
            b='девять'
        elif years_old%10==0:
            b=''
        print(a,b,m)
    else:
        print('Неправильный ввод числа')


def elif17(int_number):
    if 10<=int_number<=40:
        if (int_number%10==1) and (int_number!=11):
            m='учебное задание'
        elif (int_number%10>1) and (int_number%10<5) and (int_number!=12) and (int_number!=13) and (int_number!=14):
            m='учебных задания'
        else:
            m='учебных заданий'
        if int_number<20:
            if int_number==19:
                a='девятьнадцать'
                b=''
            elif int_number==18:
                a='восемьнадцать'
                b=''
            elif int_number==17:
                a='семьнадцать'
                b=''
            elif int_number==16:
                a='шестьнадцать'
                b=''
            elif int_number==15:
                a='пятьнадцать'
                b=''
            elif int_number==14:
                a='четырнадцать'
                b=''
            elif int_number==13:
                a='тринадцать'
                b=''
            elif int_number==12:
                a='двенадцать'
                b=''
            elif int_number==11:
                a='одиннадцать'
                b=''
            elif int_number==10:
                a='десять'
                b=''
        if int_number>=20:
            if int_number//10==2:
                a='двадцать'
            elif int_number//10==3:
                a='тридцать'
            elif int_number//10==4:
                a='сорок'
            if int_number%10==1:
                b='одно'
            elif int_number%10==2:
                b='два'
            elif int_number%10==3:
                b='три'
            elif int_number%10==4:
                b='четыре'
            elif int_number%10==5:
                b='пять'
            elif int_number%10==6:
                b='шесть'
            elif int_number%10==7:
                b='семь'
            elif int_number%10==8:
                b='восемь'
            elif int_number%10==9:
                b='девять'
            elif int_number%10==0:
                b=''
        print(a,b,m)
    else:
        print('Неправильный ввод числа')


def elif18(int_number):
    a1=int_number//100
    a2=int_number%100
    b1=int_number%100
    b2=b1//10
    c1=b1%10
    if a1==1:
        a='сто'
    if a1==2:
        a='двести'
    if a1==3:
        a='триста'
    if a1==4:
        a='четыреста'
    if a1==5:
        a='пятьсот'
    if a1==6:
        a='шестьсот'
    if a1==7:
        a='семьсот'
    if a1==8:
        a='восемьсот'
    if a1==9:
        a='девятьсот'
        
    if b2==1:
        b='десять'
    if b2==2:
        b='двадцать'
    if b2==3:
        b='тридцать'
    if b2==4:
        b='сорок'
    if b2==5:
        b='пятьдесят'
    if b2==6:
        b='шестьдесят'
    if b2==7:
        b='семьдесят'
    if b2==8:
        b='восемьдесят'
    if b2==9:
        b='девяносто'
    if b2==1 and int_number%10!=0:
        c=''
        if a2==19:
            b='девятьнадцать'
        elif a2==18:
            b='восемьнадцать'
        elif a2==17:
            b='семьнадцать'
        elif a2==16:
            b='шестьнадцать'
        elif a2==15:
            b='пятьнадцать'
        elif a2==14:
            b='четырнадцать'
        elif a2==13:
            b='тринадцать'
        elif a2==12:
            b='двенадцать'
        elif a2==11:
            b='одиннадцать'
    if b2!=1 and int_number%10!=0:
        if c1==1:
            c='один'
        elif c1==2:
            c='два'
        elif c1==3:
            c='три'
        elif c1==4:
            c='четыре'
        elif c1==5:
            c='пять'
        elif c1==6:
            c='шесть'
        elif c1==7:
            c='семь'
        elif c1==8:
            c='восемь'
        elif c1==9:
            c='девять'

    
    if c1==0:
         c=''
    if b2==0:
        b=''
    print(a,b,c)

def elif19(year):
    c=['Зелёного','Красного','Желтого','Белого','Чёрного']
    c1=['Зеленой','Красной',"Желтой",'Белой','Чёрной']
    a=['крысы','быка','тигра','кролика','дракона','змеи','коня','овцы','обезьяны','курицы','собаки','свиньи']
    year=abs(1984-year)
    while year>60:
        year=year-60
    for i in range(0,5):
        for i1 in range(0,12):
            if 12*i+i1==year:
                if year%12 in (1,2,3,4):
                    print(c[i],a[i1])
                elif year%12 in (0,5,6,7,8,9,10,11):
                    print(c1[i],a[i1])
                else:
                    print('Ошибка')
        


def elif20(day, month):
    if (day in range(20,31) and month==1) or (day in range (1,18) and month==2):
        a='Водолей'
    elif (day in range (19,28) and month==2) or (day in range(1,20) and month==3):
        a='Рыбы'
    elif (day in range (21,31) and month==3) or (day in range(1,19) and month==4):
        a='Овен'
    elif (day in range (20,30) and month==4) or (day in range(1,20) and month==5):
        a='Телец'
    elif (day in range (21,31) and month==5) or (day in range(1,21) and month==6):
        a='Близнецы'
    elif (day in range (22,30) and month==6) or (day in range(1,22) and month==7):
        a='Рак'
    elif (day in range (23,31) and month==7) or (day in range(1,22) and month==8):
        a='Лев'
    elif (day in range (23,31) and month==8) or (day in range(1,22) and month==9):
        a='Дева'
    elif (day in range (23,30) and month==9) or (day in range(1,22) and month==10):
        a='Весы'
    elif (day in range (23,31) and month==10) or (day in range(1,22) and month==11):
        a='Скорпион'
    elif (day in range (23,30) and month==11) or (day in range(1,21) and month==12):
        a='Стрелец'
    elif (day in range (22,31) and month==12) or (day in range(1,19) and month==1):
        a='Козерог'
    else:
        a='Неправильный ввод числа'
    print(a)
