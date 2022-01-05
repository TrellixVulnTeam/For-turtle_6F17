from datetime import date


def ext_25_3(mm, dd):
    try:
        d = date(2018, mm, dd)
        d1 = date(2019, 1, 1)

        a = (d1 - d).days

        if a % 10 == 1:
            print("Осталось", a, "день до Нового Года")
        elif 1 < a % 10 < 5:
            print("Осталось", a, "дня до Нового Года")
        else:
            print("Осталось", a, "дней до Нового Года")
    except ValueError:
        print('Некорректная дата')


def uses_25_3(mm, dd):
    c = 365 - dd + 1
    if mm == 1 and 1 <= dd <= 31:
        print_ansk(c)
    elif mm == 2 and 1 <= dd <= 28:
        c -= 31
        print_ansk(c)
    elif mm == 3:
        c -= 59
        print_ansk(c)
    elif mm == 4:
        c -= 90
        print_ansk(c)
    elif mm == 5:
        c -= 120
        print_ansk(c)
    elif mm == 6:
        c -= 151
        print_ansk(c)
    elif mm == 7:
        c -= 181
        print_ansk(c)
    elif mm == 8:
        c -= 212
        print_ansk(c)
    elif mm == 9:
        c -= 243
        print_ansk(c)
    elif mm == 10:
        c -= 273
        print_ansk(c)
    elif mm == 11:
        c -= 304
        print_ansk(c)
    elif mm == 12:
        c -= 334
        print_ansk(c)
    else:
        print('Некорректная дата')


def print_ansk(c):
    if (c % 100 > 10) and (c % 100 < 20):
        print('До нового года осталось ', c, ' дней')
    elif c % 10 == 1:
        print('До нового года остался ', c, ' день')
    elif 2 <= c % 10 <= 4:
        print('До нового года осталось ', c, ' дня')
    elif c % 10 in (0, 5, 6, 7, 8, 9):
        print('До нового года осталось ', c, ' дней')


for i in (12, 25), (1, 1), (2, 31):
    uses_25_3(*i)
