def change(s,i,a):              # функция замены символа в строке
    return s[:i] + a + s[i+1:]
    
s = input('Введите строку из русских букв: ')
for i in range(len(s)):
    if s[i] == 'а':
        s = change(s,i,'о')
print('Строка после замены: ',s)
