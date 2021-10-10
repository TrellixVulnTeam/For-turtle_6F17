def dict_write(aux):
    dict_file = open("dictionary_refactoring.lib", "w", encoding="utf-8")
    for key, val in aux.items():
        dict_file.write(f'{key}***{val}')
    dict_file.close()


def dict_read():
    aux = {}
    dict_file = open("dictionary_refactoring.lib", "r", encoding="utf-8")
    for line in dict_file:
        if line == '\n':
            continue
        records = line.split("***")
        aux[records[0]] = records[1]
    dict_print(aux)
    dict_file.close()
    return aux


def dict_print(aux):
    for key, val in aux.items():
        print(f'{key} - {val}', end="")
    print()


def word_fine(aux):
    word = input("Введите английское слово ")

    while word == "":
        word = input("Введите английское слово ")
        
    if word in aux:
        print(f'английское слово {word} имеет значение {aux[word]}')
    else:
        print("Такого слова нет в словаре. Можете его добавить")


def word_add(aux):
    word = input("Какое английское слово будем добавлять? ")
    if word in aux:
        print("Есть такое слоово, оно имеет значение", aux[word])
    else:
        word_translate = input("Русское значение слова " + str(word) + " будет ")
        aux[word] = word_translate


dictionary = dict_read()


answer = 1
while answer != 4:
    print("""Меню словаря:
    1. Найти слово в словаре
    2. Добавить слово в словарь
    3. Напечатать словарь
    4. Выход""")

    answer = input("Что будем делать? ")
    if answer == "":
        continue
    if answer == "1":
        word_fine(dictionary)
    elif answer == "2":
        word_add(dictionary)
    elif answer == "3":
        dict_print(dictionary)
    elif answer == "4":
        dict_write(dictionary)
        break
    else:
        print("Такой команды нет")
    
