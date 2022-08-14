global словарь
словарь={}

def запись_словаря ():
    файл=open("словарь.txt", "w")
    for ключ, значение in словарь.items():
        файл.write(ключ+" "+значение+"\n")
    файл.close()

def чтение_словоря():
    файл=open("словарь.txt", "r")
    for строка in файл:
        if строка=='\n':
            continue
        запись=строка.split(" ")
        print(запись)
        словарь[запись[0]]=запись[1]
    файл.close()

def печать_словаря():
    for ключ, значение in словарь.items():
        print("%s - %s"%(ключ, значение),end="")

def найти_слово():
    слово=input("Введите английское слово ")
    if слово in словарь:
        print("английское слово",слово,"имеет значение",словарь[слово])
    else:
        print("Такого слова нет в словаре. Можете его добавить")

def добавить_слово():
    слово=input("Какое английское слово будем добавлять? ")
    if слово in словарь:
        print("Есть такое слоов, оно имеет значение", словарь[слово])
    else:
        перевод = input("Русское значение слова "+str(слово)+" будет ")
        словарь[слово]=перевод

чтение_словоря()

ответ=1
while ответ != 4:
    print("""Меню словаря:
    Для уроков (составитель тестов). Найти слово в словаре
    2. Добавить слово в словарь
    3. Напечатать словарь
    4. Выход""")

    ответ=int(input("Что будем делать? "))

    if ответ == 1 :
        найти_слово()
    elif ответ == 2:
        добавить_слово()
    elif ответ == 3:
        печать_словаря()
    elif ответ == 4:
        запись_словаря ()
    else:
        print("Такой команды нет")
    
