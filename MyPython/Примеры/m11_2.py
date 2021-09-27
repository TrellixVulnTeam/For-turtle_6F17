# Создадим пустой словать Capitals
Capitals = {}

# Заполним его несколькими значениями
Capitals['Россия'] = 'Москва'
Capitals['Украина'] = 'Киев'
Capitals['США'] = 'Вашингтон'
Capitals['Белоруссия'] = 'Минск'
Capitals['Франция'] = 'Париж'
Capitals['Испания'] = 'Мадрид'
Capitals['Италия'] = 'Рим'

# Считаем название страны
country = input('Название страны, в которой вы живете: ')

# Проверим, есть ли такая страна в словаре Capitals
if country in Capitals:
    # Если есть - выведем ее столицу
    print('Столица вашей страны - ', Capitals[country])
else:
    # Запросим название столицы и добавив его в dictionary
    city = input('Как называется столица этой страны: ')
    Capitals[country] = city
    print('Добавили... ', country,Capitals[country])
