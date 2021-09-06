# Программа подготовлена И.В. Библовым
# Выводит случайные страницы с сайта vk.com

from webbrowser import open_new
from random import randrange

for i in range(10):
    club_id = randrange(40000000,60000000)
    open_new('http://vk.com/club%s' % club_id)
    
