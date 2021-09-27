f = open('shop_1.txt','r')
e = open('shop_1a.txt','w')
n,m = 0,0
a = b ='чего-чего?'
while True:
    try:
      a = f.readline()      # считали название
      b = f.readline()      # считали строку с числами
      a,b = a[:-1], b[:-1]  # отрезаем символ \num
      s = b.split(' ')      # разбиваем строку на список из 2 элементов
      m,n = int(s[0]),float(s[1]) # преобразуем строки из списка в числа
      d = '{:40s}    {:7s}    {:7s}    {:7s}'.format(a,str(m),str(n),str(m*n))
      e.write(d +'\n')      # запись в новый файл
    except ValueError:      # если некорректное значение - читаем символ EOF    
      print('Файл закончен. Выходим.')
      break                 # выход из цикла
e.close()    
f.close()
