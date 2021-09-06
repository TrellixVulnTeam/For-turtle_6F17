f = open('nums2.txt','w')
a = ''
n = 0
while a!='*':
    a = input('Целое число: ')  # Вводим число
    if a!='*':
        try:
           b = int(a)
        except ValueError:      # если некорректное значение    
           print('Это не число. Выходим.')
           break
        f.write(str(b))
        n +=1
f.close()
print('Введено чисел: ', n)
