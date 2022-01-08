f = open('numbers.txt', 'r')
sum = 0
for line in f:
    try:
      a = float(line)       # действие
      print(a)
    except ValueError:      # если некорректное значение    
      print('Это не число. Выходим.')
    sum += a
f.close()
print ('%10.3f' % sum)
