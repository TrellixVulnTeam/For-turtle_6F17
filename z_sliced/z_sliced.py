def elif12(number, element):
    """
    Elif12. Элементы окружности пронумерованы следующим образом:
    1 - радиус r, 2 - диаметр d = 2 * r, 3 - длина l = 2 * pi * r, 4 - площадь круга s = pi * r**2 .
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данной окружности (в том же порядке). В качестве значения π использовать 3.14.
    """
    if element == 1:
        print("r=", number, "\n", "d=", number * 2, "\n", "l=", number * 6.28, "\n", "s=", 3.14 * number ** 2)
    elif element == 2:
        print("r=", number / 2, "\n", "d=", number, "\n", "l=", number / 2 * 6.28, "\n", "s=",
              3.14 * ((number / 2) ** 2))
    elif element == 3:
        l3 = number / 6.28
        print("r=", l3, "\n", "d=", l3 * 2, "\n", "l=", number, "\n", "s=", 3.14 * l3 ** 2)
    elif element == 4:
        s4 = (number / 3.14) ** 0.5
        print("r=", s4, "\n", "d=", s4 * 2, "\n", "l=", s4 * 6.28, "\n", "s=", number)


def elif13(number, element):
    """
    Elif13. Элементы равнобедренного прямоугольного треугольника пронумерованы следующим образом:
    1 - катет a, 2 - гипотенуза c = a * 2**0.5, 3 - высота h, опущенная на гипотенузу (h = c / 2),
    4 - площадь s = c * h / 2. Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке).
    """
    if element == 1:
        c1 = number * (2 ** 0.5)
        print(" катет=", number, "\n", "гипотенуза=", c1, "\n", "высота=", c1 / 2, "\n", "площадь=", c1 * (c1 / 4))
    elif element == 2:
        print(" катет=", number / (2 ** 0.5), "\n", "гипотенуза=", number, "\n", "высота=", number / 2, "\n",
              "площадь=", number * (number / 4))
    elif element == 3:
        print(" катет=", (2 * number) / (2 ** 0.5), "\n", "гипотенуза=", 2 * number, "\n", "высота=", number, "\n",
              "площадь=", 2 * number * (number / 2))
    elif element == 4:
        gipotenusa = (number * 4) ** 0.5
        print(" катет=", gipotenusa / (2 ** 0.5), "\n", "гипотенуза=", gipotenusa, "\n", "высота=", gipotenusa / 2,
              "\n", "площадь=", number)


def elif14(number, element):
    """
    Elif14. Элементы равностороннего треугольника пронумерованы следующим образом:
    1 - сторона a, 2 - радиус r1 вписанной окружности (r1 = a * 3**0.5 / 6),
    3 - радиус r2 описанной окружности (r2 = 2 * r1), 4 - площадь s = a**2 * 3**0.5 / 4.
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке)"""
    if element == 1:
        print(" сторона=", number, "\n", "радиус r1 =", number * (3 ** 0.5 / 6), "\n", "радиус r2=",
              2 * number * (3 ** 0.5 / 6), "\n", "площадь=", (number ** 2) * (3 ** 0.5 / 4))
    elif element == 2:
        r1 = number / (3 ** 0.5 / 6)
        print(" сторона=", r1, "\n", "радиус r1 =", number, "\n", "радиус r2=", 2 * number, "\n", "площадь=",
              r1 ** 2 * (3 ** 0.5 / 4))
    elif element == 3:
        r11 = (number / 2) / (3 ** 0.5 / 6)
        print(" сторона=", r11, "\n", "радиус r1 =", number / 2, "\n", "радиус r2=", number, "\n", "площадь=",
              r11 * (3 ** 0.5 / 4))
    elif element == 4:
        a = (number / (3 ** 0.5 / 4)) ** 0.5
        print(" сторона=", a, "\n", "радиус r1 =", a * (3 ** 0.5 / 6), "\n", "радиус r2=", 2 * a * (3 ** 0.5 / 6), "\n",
              "площадь=", number)


def elif15(n, m):
    """
    Elif15. Мастям игральных карт присвоены порядковые номера: 1 - пики, 2 - трефы, 3 - бубны, 4 - червы.
    Достоинству карт, старших десятки, присвоены номера: 11 - валет, 12 - дама, 13 - король, 14 - туз.
    Даны два целых числа: n - достоинство (6 ≤ N ≤ 14) и m - масть карты (1 ≤ M ≤ 4).
    Вывести название соответствующей карты вида «шестерка бубен», «дама червей», «туз треф» и т. п.
    """
    if n == 6:
        print("шестёрка", end=" ")
    elif n == 7:
        print("семёрка", end=" ")
    elif n == 8:
        print("восьмёрка", end=" ")
    elif n == 9:
        print("девятка", end=" ")
    elif n == 10:
        print("десятка", end=" ")
    elif n == 11:
        print("валет", end=" ")
    elif n == 12:
        print("дама", end=" ")
    elif n == 13:
        print("король", end=" ")
    elif n == 14:
        print("туз", end=" ")

    if m == 1:
        print("пик")
    elif m == 2:
        print("треф")
    elif m == 3:
        print("бубен")
    elif m == 4:
        print("червей")


def elif16(years_olds):
    """
    Elif16. Дано целое число в диапазоне 20–69, определяющее возраст (в годах).
    Вывести строку-описание указанного возраста, обеспечив правильное согласование числа со словом «год»,
    например: 20 - «двадцать лет», 32 - «тридцать два года», 41 - «сорок один год».
    """
    if years_olds // 10 == 2:
        print("двадцать", end=" ")
    elif years_olds // 10 == 3:
        print("тридцать", end=" ")
    elif years_olds // 10 == 4:
        print("сорок", end=" ")
    elif years_olds // 10 == 5:
        print("пятьдесят", end=" ")
    elif years_olds // 10 == 6:
        print("шестьдесят", end=" ")

    if years_olds % 10 == 0:
        print("лет")
    elif years_olds % 10 == 1:
        print("один год")
    elif years_olds % 10 == 2:
        print("два года")
    elif years_olds % 10 == 3:
        print("три года")
    elif years_olds % 10 == 4:
        print("четыре года")
    elif years_olds % 10 == 5:
        print("пять лет")
    elif years_olds % 10 == 6:
        print("шесть лет")
    elif years_olds % 10 == 7:
        print("семь лет")
    elif years_olds % 10 == 8:
        print("восемь лет")
    elif years_olds % 10 == 9:
        print("девять лет")


def elif17(int_number):
    """
    Elif17. Дано целое число в диапазоне 10–40, определяющее количество учебных заданий по некоторой теме.
    Вывести строку-описание указанного количества заданий, обеспечив правильное согласование числа со словами
    «учебное задание», например: 18 - «восемнадцать учебных заданий», 23 - «двадцать три учебных задания»,
    31 - «тридцать одно учебное задание».
   """
    if int_number == 10:
        print("десять", end=" ")
    elif int_number == 11:
        print("одиннадцать", end=" ")
    elif int_number == 12:
        print("двенадцать", end=" ")
    elif int_number == 13:
        print("тринадцать", end=" ")
    elif int_number == 14:
        print("четырнадцать", end=" ")
    elif int_number == 15:
        print("пятнадцать", end=" ")
    elif int_number == 16:
        print("шестнадцать", end=" ")
    elif int_number == 17:
        print("семнадцать", end=" ")
    elif int_number == 18:
        print("восемнадцать", end=" ")
    elif int_number == 19:
        print("девятнадцать", end=" ")

    if int_number // 10 == 2:
        print("двадцать", end=" ")
    elif int_number // 10 == 3:
        print("тридцать", end=" ")
    elif int_number // 10 == 4:
        print("сорок", end=" ")

    if int_number // 10 == 1:
        print("учебных заданий")
    elif int_number % 10 == 1:
        print("одно учебное задание")
    elif int_number % 10 == 2:
        print("два учебных заданий")
    elif int_number % 10 == 3:
        print("три учебных заданий")
    elif int_number % 10 == 4:
        print("четыре учебных заданий")
    elif int_number % 10 == 5:
        print("пять учебных заданий")
    elif int_number % 10 == 6:
        print("шесть учебных заданий")
    elif int_number % 10 == 7:
        print("семь учебных заданий")
    elif int_number % 10 == 8:
        print("восемь учебных заданий")
    elif int_number % 10 == 9:
        print("девять учебных заданий")
    elif int_number % 10 == 0:
        print("учебных заданий")


def elif18(int_number):
    """
    Elif18. Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа,
    например: 256 - «двести пятьдесят шесть», 814 - «восемьсот четырнадцать».
    """
    if int_number // 100 == 1:
        print("сто", end=" ")
    elif int_number // 100 == 2:
        print("двести", end=" ")
    elif int_number // 100 == 3:
        print("триста", end=" ")
    elif int_number // 100 == 4:
        print("четыреста", end=" ")
    elif int_number // 100 == 5:
        print("пятьсот", end=" ")
    elif int_number // 100 == 6:
        print("шестьсот", end=" ")
    elif int_number // 100 == 7:
        print("семьсот", end=" ")
    elif int_number // 100 == 8:
        print("восемьсот", end=" ")
    elif int_number // 100 == 9:
        print("девятьсот", end=" ")

    if int_number % 100 // 10 == 0:
        print(end="")
    elif int_number % 100 // 10 == 2:
        print("двадцать", end=" ")
    elif int_number % 100 // 10 == 3:
        print("тридцать", end=" ")
    elif int_number % 100 // 10 == 4:
        print("сорок", end=" ")
    elif int_number % 100 // 10 == 5:
        print("пятьдесят", end=" ")
    elif int_number % 100 // 10 == 6:
        print("шестьдесят", end=" ")
    elif int_number % 100 // 10 == 7:
        print("семьдесят", end=" ")
    elif int_number % 100 // 10 == 8:
        print("восемдесят", end=" ")
    elif int_number % 100 // 10 == 9:
        print("девяносто", end=" ")

    elif int_number % 100 == 10:
        print("десять", end=" ")
    elif int_number % 100 == 11:
        print("одиннадцать", end=" ")
    elif int_number % 100 == 12:
        print("двенадцать", end=" ")
    elif int_number % 100 == 13:
        print("тринадцать", end=" ")
    elif int_number % 100 == 14:
        print("четырнадцать", end=" ")
    elif int_number % 100 == 15:
        print("пятнадцать", end=" ")
    elif int_number % 100 == 16:
        print("шестнадцать", end=" ")
    elif int_number % 100 == 17:
        print("семнадцать", end=" ")
    elif int_number % 100 == 18:
        print("восемнадцать", end=" ")
    elif int_number % 100 == 19:
        print("девятнадцать", end=" ")

    if int_number % 10 == 0 and int_number % 100 // 10 != 1:
        print(end="")
    elif int_number % 10 == 1 and int_number % 100 // 10 != 1:
        print("один")
    elif int_number % 10 == 2 and int_number % 100 // 10 != 1:
        print("два")
    elif int_number % 10 == 3 and int_number % 100 // 10 != 1:
        print("три")
    elif int_number % 10 == 4 and int_number % 100 // 10 != 1:
        print("четыре")
    elif int_number % 10 == 5 and int_number % 100 // 10 != 1:
        print("пять")
    elif int_number % 10 == 6 and int_number % 100 // 10 != 1:
        print("шесть")
    elif int_number % 10 == 7 and int_number % 100 // 10 != 1:
        print("семь")
    elif int_number % 10 == 8 and int_number % 100 // 10 != 1:
        print("восемь")
    elif int_number % 10 == 9 and int_number % 100 // 10 != 1:
        print("девять")


def elif19(year):
    """
    Elif19. В восточном календаре принят 60-летний цикл, состоящий из 12-летних под-циклов,
    обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный. В каждом подцикле годы носят
    названия животных: крысы, коровы, тигра, зайца, дракона, змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи.
    По номеру года определить его название, если 1984 год - начало цикла: «год зеленой крысы».
    """
    if year % 10 == 0 or year % 10 == 1:
        print("год бело", end="")
    elif year % 10 == 2 or year % 10 == 3:
        print("год голубо", end="")
    if year % 10 == 4 or year % 10 == 5:
        print("год зелёно", end="")
    if year % 10 == 6 or year % 10 == 7:
        print("год красно", end="")
    if year % 10 == 8 or year % 10 == 9:
        print("год жёлто", end="")

    if year % 12 == 0:
        print("й обезьяны")
    elif year % 12 == 1:
        print("го петуха")
    elif year % 12 == 2:
        print("й собаки")
    elif year % 12 == 3:
        print("й свиньи")
    elif year % 12 == 4:
        print("й крысы")
    elif year % 12 == 5:
        print("го быка")
    elif year % 12 == 6:
        print("го тигра")
    elif year % 12 == 7:
        print("го кролика")
    elif year % 12 == 8:
        print("го дракона")
    elif year % 12 == 9:
        print("й змеи")
    elif year % 12 == 10:
        print("й лошади")
    elif year % 12 == 10:
        print("й овцы")


def elif20(day, month):
    """
    Elif20. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату.
    Вывести знак Зодиака, соответствующий этой дате: «Водолей» (20.1–18.2), «Рыбы» (19.2–20.3), «Овен» (21.3–19.4),
    «Телец» (20.4–20.5), «Близнецы» (21.5–21.6), «Рак» (22.6–22.7), «Лев» (23.7–22.8), «Дева» (23.8–22.9),
    «Весы» (23.9–22.10), «Скорпион» (23.10–22.11), «Стрелец» (23.11–21.12), «Козерог» (22.12–19.1)
    """
    index = month * 100 + day
    if 120 <= index <= 218:
        print("Водолей")
    elif 219 <= index <= 320:
        print("Рыбы")
    elif 321 <= index <= 419:
        print("Овен")
    elif 420 <= index <= 520:
        print("Телец")
    elif 521 <= index <= 621:
        print("Близнецы")
    elif 622 <= index <= 722:
        print("Рак")
    elif 723 <= index <= 822:
        print("Лев")
    elif 823 <= index <= 922:
        print("Дева")
    elif 923 <= index <= 1022:
        print("Весы")
    elif 1023 <= index <= 1122:
        print("Скорпион")
    elif 1123 <= index <= 1221:
        print("Стрелец")
    elif 1222 <= index <= 1231 or 101 <= index <= 129:
        print("Козерог")
    else:
        print("неверная дата или месяц")