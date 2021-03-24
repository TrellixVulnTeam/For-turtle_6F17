import random
from z_elifs import atenyaeva1 as temp1
from z_elifs import atenyaevs2 as temp2


def approx_Equal(x, y, tolerance=0.001):
    return abs(x-y) <= 0.5 * tolerance * (x + y)


def r_number(minis=-10, maxis=10):
    return random.randrange(minis, maxis)


def search_answer_numeric(teacher_answer, students_answer):
    flag = True
    for i in range(4):
        if not approx_Equal(teacher_answer[i], students_answer[i]):
            flag = False
    return flag

def search_answer(teacher_answer, students_answer):
    """
    Проверят, есть ли нужное значение в строке студента.
    :param teacher_answer: то, что возвращает эталонный алгоритм. Если не тим не строка, то преобразуем встроку
    :param students_answer: то, что возвращает программа студента. Возращает лист текстовых переменных
    :return: True если есть значения эталонного алгоритма в ответе студента и False во всех остальных случаях
    """
    students_answer = str(students_answer).lower()
    teacher_answer = str(teacher_answer).lower()
    flag = True
    for i in teacher_answer:
        if i not in students_answer:
            flag = False
    return flag


def search_answer_conveyor(teacher_answer, students_answer):
    students_answer = str(students_answer)
    teacher_answer = list(map(str, teacher_answer))

    flag = True
    for i in teacher_answer:
        if i not in students_answer:
            flag = False
    return flag


def elif_r1(int_number):
    """
    Elif1. Дано целое число в диапазоне 1–7. Вывести строку - название дня недели,
    соответствующее данному числу (1 - «понедельник», 2 - «вторник» и т. д.), иначе
    вывести "0"
    """
    week_days = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
    if 1 <= int_number <= 7:
        return week_days[int_number-1]
    else:
        return 0


def elif_r2(k):
    """
    Elif2. Дано целое число k. Вывести строку-описание оценки, соответствующей числу k
    (1 - «плохо», 2 - «неудовлетворительно», 3 - «удовлетворительно», 4 - «хорошо», 5 - «отлично»).
    Если k не лежит в диапазоне 1–5, то вывести строку «ошибка».
    """
    week_days = ('плохо', 'неудовлетворительно', 'удовлетворительно', 'хорошо', 'отлично')
    if 1 <= k <= 5:
        return week_days[k-1]
    else:
        return 'ошибка'


def elif_r3(month):
    """
    Elif3. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Вывести название соответствующего времени года («зима», «весна», «лето», «осень»).
    """
    winter = (1, 2, 12)
    spring = (3, 4, 5)
    summer = (6, 7, 8)
    autumn = (9, 10, 11)

    if month in winter:
        return 'зима'
    elif month in spring:
        return 'весна'
    elif month in summer:
        return 'лето'
    elif month in autumn:
        return 'осень'
    else:
        return 0


def elif_r4(month):
    """
    Elif4. Дан номер месяца - целое число в диапазоне 1–12 (1 - январь, 2 - февраль и т. д.).
    Определить количество дней в этом месяце для невисокосного года.
    """
    thirty_one = (1, 3, 5, 7, 8, 10, 12)
    thirty = (4, 6, 9, 11)
    if month in thirty_one:
        return 31
    elif month in thirty:
        return 30
    elif month == 2:
        return 28
    else:
        return 0


def elif_r5(n, a, b):
    """
    Elif5. Арифметические действия над числами пронумерованы следующим образом:
    1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
    Дан номер действия n (целое число в диапазоне 1–4) и вещественные числа a и b (b не равно 0).
    Выполнить над числами указанное действие и вывести результат.
    """
    if n == 1:
        return a + b
    elif n == 2:
        return a - b
    elif n == 3:
        return a * b
    elif n == 4:
        if b == 0:
            return "Деление на ноль неопределено"
        else:
            return a / b


def elif_r6(number, length):
    """
    Elif6. Единицы длины пронумерованы следующим образом:
    1 - дециметр, 2 - километр, 3 - метр, 4 - миллиметр, 5 - сантиметр.
    Дан номер единицы длины (целое число в диапазоне 1–5) и длина отрезка в этих единицах (вещественное число).
    Найти длину отрезка в метрах.
    """
    res = None
    if number == 1:
        res = length / 10
    elif number == 2:
        res = length * 1000
    elif number == 3:
        res = length
    elif number == 4:
        res = length / 1000
    elif number == 5:
        res = length / 100
    return res


def elif_r7(number, mass):
    """
    Elif7. Единицы массы пронумерованы следующим образом:
    1 - килограмм, 2 - миллиграмм, 3 - грамм, 4 - тонна, 5 - центнер.
    Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
    Найти массу тела в килограммах.
    """
    m = None
    if number == 1:
        m = mass
    elif number == 2:
        m = mass / 1000000
    elif number == 3:
        m = mass / 1000
    elif number == 4:
        m = mass * 1000
    elif number == 5:
        m = mass * 100
    return m


def elif_r8(day, month):
    """
    Elif8. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, предшествующей указанной.
    """
    max_day = elif_r4(month)
    if day > max_day:
        return 0, 0
    else:
        if day > 1:
            day -= 1
        else:
            if month == 1:
                month = 12
            else:
                month -= 1
                day = elif_r4(month)

        return day, month


def elif_r9(day, month):
    """
    Elif9. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату невисокосного года.
    Вывести значения day и month для даты, следующей за указанной.
    """
    max_day = elif_r4(month)
    if day > max_day:
        return 0, 0
    else:
        if day < max_day:
            day += 1
        else:
            day = 1
            if month == 12:
                month = 1
            else:
                month += 1
        return day, month


def elif_r10(symbol, int_number):
    """
    Elif10. Робот может перемещаться в четырех направлениях («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и принимать три цифровые команды: 0 - продолжать движение, 1 - поворот налево, −1 - поворот направо.
    Дан символ symbol - исходное направление робота и целое число int_number - посланная ему команда.
    Вывести направление робота после выполнения полученной команды.
    """
    direction = ('С', 'З', 'Ю', 'В')
    robot_direction = direction.index(symbol)
    if int_number == 1:
        if 0 <= robot_direction <= 2:
            symbol = direction[robot_direction + 1]
        else:
            symbol = direction[0]
    elif int_number == -1:
        if 1 <= robot_direction <= 3:
            symbol = direction[robot_direction - 1]
        else:
            symbol = direction[3]

    return symbol


def elif_r11(symbol, int1, int2):
    """
    Elif11. Локатор ориентирован на одну из сторон света («С» - север, «З» - запад, «Ю» - юг, «В» - восток)
    и может принимать три цифровые команды поворота: 1 - поворот налево, −1 - поворот направо, 2 - поворот на 180.
    Дан символ symbol - исходная ориентация локатора и целые числа int1 и int2 - две посланные команды.
    Вывести ориентацию локатора после выполнения этих команд.
    """
    direction = ('С', 'З', 'Ю', 'В')
    radar_direction = direction.index(symbol)
    for i in int1, int2:
        if i == 1:
            radar_direction = (radar_direction + 1) % 4
        elif i == -1:
            radar_direction = (radar_direction - 1) % 4
        elif i == 2:
            radar_direction = (radar_direction + 2) % 4

    return direction[radar_direction]


def elif_r12(element, number):
    """
    Elif12. Элементы окружности пронумерованы следующим образом:
    1 - радиус r, 2 - диаметр d = 2 * r, 3 - длина l = 2 * pi * r, 4 - площадь круга s = pi * r**2 .
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данной окружности (в том же порядке). В качестве значения π использовать 3.14.
    """
    if element == 1:
        r = number
        d = 2 * r
        length = 2 * 3.14 * r
        s = 3.14 * r ** 2
    elif element == 2:
        d = number
        r = d / 2
        length = 2 * 3.14 * r
        s = 3.14 * r ** 2
    elif element == 3:
        length = number
        r = length / 2 / 3.14
        d = 2 * r
        s = 3.14 * r ** 2
    elif element == 4:
        s = number
        r = (s / 3.14)**0.5
        d = 2 * r
        length = 2 * 3.14 * r
    else:
        r = length = d = s = 0
    return r, length, d, s


def elif_r13(element, number):
    """
    Elif13. Элементы равнобедренного прямоугольного треугольника пронумерованы следующим образом:
    1 - катет a, 2 - гипотенуза c = a * 2**0.5, 3 - высота h, опущенная на гипотенузу (h = c / 2),
    4 - площадь s = c * h / 2. Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке).
    """
    if element == 1:
        a = number
        c = a * 2**0.5
        h = c / 2
        s = c * h / 2
    elif element == 2:
        c = number
        a = c / 2**0.5
        h = c / 2
        s = c * h / 2
    elif element == 3:
        h = number
        c = 2 * h
        a = c / 2**0.5
        s = c * h / 2
    elif element == 4:
        s = number
        c = (s * 4)**0.5
        a = c / 2**0.5
        h = c / 2
    else:
        s = c = a = h = 0
    return a, c, h, s


def elif_r14(element, number):
    """
    Elif14. Элементы равностороннего треугольника пронумерованы следующим образом:
    1 - сторона a, 2 - радиус r1 вписанной окружности (r1 = a * 3**0.5 / 6),
    3 - радиус r2 описанной окружности (r2 = 2 * r1), 4 - площадь s = a**2 * 3**0.5 / 4.
    Дан номер одного из этих элементов и его значение.
    Вывести значения остальных элементов данного треугольника (в том же порядке).
    """
    if element == 1:
        a = number
        r1 = a * 3**0.5 / 6
        r2 = r1 * 2
        s = a**2 * 3**0.5 / 4
    elif element == 2:
        r1 = number
        a = r1 * 6 / 3**0.5
        r2 = r1 * 2
        s = a**2 * 3**0.5 / 4
    elif element == 3:
        r2 = number
        r1 = r2 / 2
        a = r1 * 6 / 3**0.5
        s = a**2 * 3**0.5 / 4
    elif element == 4:
        s = number
        a = (s * 4 / 3**0.5)**0.5
        r1 = a * 3**0.5 / 6
        r2 = r1 * 2
    else:
        a = r1 = r2 = s = 0
    return a, r1, r2, s


def elif_r15(n, m):
    """
    Elif15. Мастям игральных карт присвоены порядковые номера: 1 - пики, 2 - трефы, 3 - бубны, 4 - червы.
    Достоинству карт, старших десятки, присвоены номера: 11 - валет, 12 - дама, 13 - король, 14 - туз.
    Даны два целых числа: n - достоинство (6 ≤ N ≤ 14) и m - масть карты (1 ≤ M ≤ 4).
    Вывести название соответствующей карты вида «шестерка бубен», «дама червей», «туз треф» и т. п.
    """
    suit = ('пики', 'треф', 'бубен', 'червей')
    value = ('шестерка ', 'семерка ', 'восьмерка ', 'девятка ', 'десятка ', 'валет ', 'дама ', 'король ', 'туз ')

    if 6 <= n <= 14 and 1 <= m <= 4:
        return value[n - 6] + suit[m - 1]
    else:
        return 0


def elif_r16(years_olds):
    """
    Elif16. Дано целое число в диапазоне 20–69, определяющее возраст (в годах).
    Вывести строку-описание указанного возраста, обеспечив правильное согласование числа со словом «год»,
    например: 20 - «двадцать лет», 32 - «тридцать два года», 41 - «сорок один год».
    """
    tens = ('двадцать ', 'тридцать ', 'сорок ', 'пятьдесят ', 'шестьдесят ')
    ones = ('один год', 'два года', 'три года', 'четыре года', 'пять лет', 'шесть лет',
            'семь лет', 'восемь лет', 'девять лет')
    ten = years_olds // 10
    one = years_olds % 10
    if 20 <= years_olds <= 69:
        if one == 0:
            return tens[ten - 2] + 'лет'
        else:
            return tens[ten - 2] + ones[one - 1]
    else:
        return 0


def elif_r17(int_number):
    """
    Elif17. Дано целое число в диапазоне 10–40, определяющее количество учебных заданий по некоторой теме.
    Вывести строку-описание указанного количества заданий, обеспечив правильное согласование числа со словами
    «учебное задание», например: 18 - «восемнадцать учебных заданий», 23 - «двадцать три учебных задания»,
    31 - «тридцать одно учебное задание».
   """

    teens = ('одиннадцать ', 'двенадцать ', 'тринадцать ', 'четырнадцать ', 'пятнадцать ', 'шестнадцать ',
             'семнадцать ', 'восемнадцать ', 'девятнадцать ')
    tens = ('десять ', 'двадцать ', 'тридцать ', 'сорок ')
    ones = ('одно учебное задание', 'два учебных задания', 'три учебных задания', 'четыре учебных задания',
            'пять учебных заданий', 'шесть учебных заданий', 'семь учебных заданий', 'восемь учебных заданий',
            'девять учебных заданий')
    ten = int_number // 10
    one = int_number % 10
    if 10 < int_number < 20:
        return teens[int_number - 11] + 'учебных заданий'
    else:
        if one == 0:
            return tens[ten - 1] + 'учебных заданий'
        else:
            return tens[ten - 1] + ones[one - 1]


def elif_r18(int_number):
    """
    Elif18. Дано целое число в диапазоне 1–999. Вывести строку-описание данного числа,
    например: 256 - «двести пятьдесят шесть», 814 - «восемьсот четырнадцать».
    """
    ones = ('один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')
    teens = ('одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
             'восемнадцать', 'девятнадцать')
    tens = ('десять ', 'двадцать ', 'тридцать ', 'сорок ', 'пятьдесят ', 'шестьдесят ', 'семьдесят ', 'восемьдесят ',
            'девяносто ')
    hundreds = ('сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот')
    hundred = int_number // 100
    teen = int_number % 100
    ten = (int_number % 100) // 10
    one = int_number % 10
    res = ''
    if 1 <= hundred <= 9:
        res += hundreds[hundred - 1]
    if 10 < teen < 20:
        res += ' '
        res += teens[teen - 11]
    else:
        if 1 <= ten <= 9:
            res += ' '
            res += tens[ten - 1]
    if 1 <= one <= 9:
        res += ' '
        res += ones[one - 1]
    return res


def elif_r19(year):
    """
    Elif19. В восточном календаре принят 60-летний цикл, состоящий из 12-летних под-циклов,
    обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный. В каждом подцикле годы носят
    названия животных: крысы, коровы, тигра, зайца, дракона, змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи.
    По номеру года определить его название, если 1984 год - начало цикла: «год зеленой крысы».
    """
    res = 'год '
    zoos = ('крысы', 'коровы', 'тигра', 'зайца', 'дракона', 'змеи', 'лошади', 'овцы', 'обезьяны', 'курицы', 'собаки',
            'свиньи')
    color_oy = ('зеленой ', 'красной ', 'желтой ', 'белой ', 'черной ')
    color_ogo = ('зеленого ', 'красного ', 'желтого ', 'белого ', 'черного ')
    zoo = (year % 12 - 4) % 12
    color = (year % 5 - 4) % 5
    if zoo in [3, 4, 5]:
        res += color_ogo[color]
    else:
        res += color_oy[color]
    res += zoos[zoo]
    return res


def elif_r20(day, month):
    """
    Elif20. Даны два целых числа: day (день) и month (месяц), определяющие правильную дату.
    Вывести знак Зодиака, соответствующий этой дате: «Водолей» (20.1–18.2), «Рыбы» (19.2–20.3), «Овен» (21.3–19.4),
    «Телец» (20.4–20.5), «Близнецы» (21.5–21.6), «Рак» (22.6–22.7), «Лев» (23.7–22.8), «Дева» (23.8–22.9),
    «Весы» (23.9–22.10), «Скорпион» (23.10–22.11), «Стрелец» (23.11–21.12), «Козерог» (22.12–19.1)
    """
    day_control = day <= elif_r4(month)
    if month == 2:
        day_control = day <= elif_r4(month) + 1
    if month in range(1, 13) and day_control:
        x = month * 100 + day
        if x in range(101, 120):
            return 'Козерог'
        elif x in range(120, 218+1):
            return 'Водолей'
        elif x in range(219, 321):
            return 'Рыбы'
        elif x in range(321, 420):
            return 'Овен'
        elif x in range(420, 521):
            return 'Телец'
        elif x in range(521, 622):
            return 'Близнецы'
        elif x in range(622, 723):
            return 'Рак'
        elif x in range(723, 823):
            return 'Лев'
        elif x in range(823, 923):
            return 'Дева'
        elif x in range(923, 1023):
            return 'Весы'
        elif x in range(1023, 1123):
            return 'Скорпион'
        elif x in range(1123, 1222):
            return 'Стрелец'
        elif x in range(1222, 1232):
            return 'Козерог'
    else:
        return 0

def test():
    flag = True
    for i in range(10):
        a = r_number(1, 8)
        if not search_answer(elif_r1(a), temp1.elif1(a)):
            flag = False
            if 1 in printing:
                print(a)
    print("Test 1 - Ok" if flag else "Test 1 - Fail")

    flag = True
    for i in range(10):
        a = r_number(1, 6)
        if not search_answer(elif_r2(a), temp1.elif2(a)):
            flag = False
            if 2 in printing:
                print(a)
    print("Test 2 - Ok" if flag else "Test 2 - Fail")

    flag = True
    for i in range(30):
        a = r_number(1, 13)
        if not search_answer(elif_r3(a), temp1.elif3(a)):
            flag = False
            if 3 in printing:
                print(a)
    print("Test 3 - Ok" if flag else "Test 3 - Fail")

    flag = True
    for i in range(30):
        a = r_number(1, 13)
        if not search_answer(elif_r4(a), temp1.elif4(a)):
            flag = False
            if 4 in printing:
                print(a, elif_r4(a), temp1.elif4(a))
    print("Test 4 - Ok" if flag else "Test 4 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 5)
        b = r_number()
        c = r_number()
        if c == 0:
            c += 1
        if not search_answer(elif_r5(a, b, c), temp1.elif5(a, b, c)):
            flag = False
            if 5 in printing:
                print((a, b, c), elif_r5(a, b, c), temp1.elif5(a, b, c))
    print("Test 5 - Ok" if flag else "Test 5 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 6)
        b = r_number(0, 10000)
        if not search_answer(elif_r6(a, b), temp1.elif6(a, b)):
            flag = False
            if 6 in printing:
                print(a, b)
    print("Test 6 - Ok" if flag else "Test 6 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 6)
        b = r_number(0, 10000)
        if not search_answer(elif_r7(a, b), temp1.elif7(a, b)):
            flag = False
            if 7 in printing:
                print(a, b)
    print("Test 7 - Ok" if flag else "Test 7 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 32)
        b = r_number(1, 13)
        if not search_answer_conveyor(elif_r8(a, b), temp1.elif8(a, b)):
            flag = False
            if 8 in printing:
                print((a, b), elif_r8(a, b), temp1.elif8(a, b))
    print("Test 8 - Ok" if flag else "Test 8 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 31)
        b = r_number(1, 13)
        if not search_answer_conveyor(elif_r9(a, b), temp1.elif9(a, b)):
            flag = False
            if 9 in printing:
                print((a, b), elif_r9(a, b), temp1.elif9(a, b))
    print("Test 9 - Ok" if flag else "Test 9 - Fail")

    flag = True
    for i in range(200):
        wegas = ('С', 'Ю', 'З', 'В')
        logos = (-1, 0, 1)
        a = random.choice(wegas)
        b = random.choice(logos)
        if not search_answer_conveyor(elif_r10(a, b), temp1.elif10(a, b)):
            flag = False
            if 10 in printing:
                print((a, b), elif_r10(a, b), temp1.elif10(a, b))
    print("Test 10 - Ok" if flag else "Test 10 - Fail")

    flag = True
    for i in range(200):
        wegas = ('С', 'Ю', 'З', 'В')
        logos = (-1, 2, 1)
        a = random.choice(wegas)
        b = random.choice(logos)
        c = random.choice(logos)
        if not search_answer_conveyor(elif_r11(a, b, c), temp1.elif11(a, b, c)):
            flag = False
            if 11 in printing:
                print((a, b, c), elif_r11(a, b, c), temp1.elif11(a, b, c))
    print("Test 11 - Ok" if flag else "Test 11 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 5)
        b = r_number(0, 100)
        if not search_answer_conveyor(elif_r12(a, b), temp2.elif12(a, b)):
            flag = False
            if 12 in printing:
                print(a, b)
    print("Test 12 - Ok" if flag else "Test 12 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 5)
        b = r_number(0, 100)
        if not search_answer_numeric(elif_r13(a, b), temp2.elif13(a, b)):
            flag = False
            if 13 in printing:
                print((a, b), elif_r13(a, b), temp2.elif13(a, b))
    print("Test 13 - Ok" if flag else "Test 13 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 5)
        b = r_number(0, 100)
        if not search_answer_numeric(elif_r14(a, b), temp2.elif14(a, b), ):
            flag = False
            if 14 in printing:
                print((a, b), elif_r14(a, b), temp2.elif14(a, b))
    print("Test 14 - Ok" if flag else "Test 14 - Fail")

    flag = True
    for i in range(200):
        a = r_number(6, 15)
        b = r_number(1, 5)
        if not search_answer_conveyor(elif_r15(a, b), temp2.elif15(a, b)):
            flag = False
            if 15 in printing:
                print((a, b), elif_r15(a, b), temp2.elif15(a, b))
    print("Test 15 - Ok" if flag else "Test 15 - Fail")

    flag = True
    for i in range(200):
        a = r_number(20, 70)
        if not search_answer_conveyor(elif_r16(a), temp2.elif16(a)):
            flag = False
            if 16 in printing:
                print(a)
    print("Test 16 - Ok" if flag else "Test 16 - Fail")

    flag = True
    for i in range(200):
        a = r_number(10, 41)
        if not search_answer_conveyor(elif_r17(a), temp2.elif17(a)):
            flag = False
            if 17 in printing:
                print(a)
    print("Test 17 - Ok" if flag else "Test 17 - Fail")

    flag = True
    for i in range(200):
        a = r_number(100, 1000)
        if not search_answer_conveyor(elif_r18(a), temp2.elif18(a)):
            flag = False
            if 18 in printing:
                print((a), elif_r18(a), temp2.elif18(a))
    print("Test 18 - Ok" if flag else "Test 18 - Fail")

    flag = True
    for i in range(200):
        a = 1984 + i
        if not search_answer_conveyor(elif_r19(a), temp2.elif19(a)):
            flag = False
            if 19 in printing:
                print((a), elif_r19(a), temp2.elif19(a))
    print("Test 19 - Ok" if flag else "Test 19 - Fail")

    flag = True
    for i in range(200):
        a = r_number(1, 32)
        b = r_number(1, 13)
        if not search_answer(elif_r20(a, b), temp2.elif20(a, b)):
            flag = False
            if 20 in printing:
                print((a, b), elif_r20(a, b), temp2.elif20(a, b))
    print("Test 20 - Ok" if flag else "Test 20 - Fail")


printing = (0, )
test()