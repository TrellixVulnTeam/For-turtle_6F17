from datetime import date

def ext_25_3 (mm, dd):

    d = date(2018, mm, dd)
    d1 = date(2019, 1, 1)

    a = (d1 - d).days

    if a % 10 == 1:
        print("Осталось", a, "день до Нового Года")
    elif 1 < a % 10 < 5:
        print("Осталось", a, "дня до Нового Года")
    else:
        print("Осталось", a, "дней до Нового Года")
