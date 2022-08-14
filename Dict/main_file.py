import read_dictionary
import write_dictionary
import fine_dictionary
import add_dictionary

dictionary = read_dictionary.function()
answer = 1

while answer != 4:
    print("""Меню словаря:
    Для уроков (составитель тестов). Найти слово в словаре
    2. Добавить слово в словарь
    3. Напечатать словарь
    4. Выход""")

    answer = input("Что будем делать? ")
    if answer == "":
        continue
    if answer == "Для уроков (составитель тестов)":
        fine_dictionary.fine_word(dictionary)
    elif answer == "2":
        add_dictionary.add_word(dictionary)
    elif answer == "3":
        read_dictionary.print_dic(dictionary)
    elif answer == "4":
        write_dictionary.exit(dictionary)
        break
    else:
        print("Такой команды нет")