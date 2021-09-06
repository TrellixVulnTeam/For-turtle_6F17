import rooms # Импорт модуля - подключаем к программе
# запрос данных у пользователя
print ("Введите размеры помещения (в метрах) ...")
l = int(input ("длина: "))
w = int(input ("ширина: "))
h = int(input ("высота: "))
 
print ("Введите данные об оконных проемах (в метрах) ...")
h_w = int(input ("высота: "))
w_w = int(input ("ширина: "))
m = int(input ("количество: "))
 
print ("Введите данные о дверных проемах (в метрах) ...")
h_d = int(input ("высота: "))
w_d = int(input ("ширина: "))
n = int(input ("количество: "))
# Создаем объект класса Room:
uroom = rooms.Room(l,w,h)
# Используем объект:
uroom.win_door(h_w, w_w, h_d, w_d, m,n)
uroom.wallpapers()
uroom.printer() 
