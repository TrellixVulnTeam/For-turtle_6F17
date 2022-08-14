файл = open("C:/Users/user205/Desktop/Pyton/Для уроков (составитель тестов).txt", "r")
сумма = 0
for строка in файл:
    print(строка, end="")
    сумма+=int(строка)
print("\n",сумма)

список=[str(i) for i in range(1,21)]
список.reverse()
print(список)
файл=open("C:/Users/user205/Desktop/Pyton/2.txt", "w")

for элемент in список:
    файл.write(элемент + "\n")
файл.close()

файл = open("C:/Users/user205/Desktop/Pyton/2.txt", "r")
for строка in файл:
    print(строка, end="")
