old = int(input("Введи возраст человека: "))
if 10 < old % 100 < 20:
    print(f"Возрвст {old} лет")
elif old % 10 == 1:
    print(f"Возрвст {old} год")
elif 1 < old % 10 < 5:
    print(f"Возрвст {old} года")
else:
    print(f"Возрвст {old} лет")



