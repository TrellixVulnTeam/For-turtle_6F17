# Пример 1
# Ввод списка
m = []
for i in range(5):
    m = m + [int(input('Число = '))]
# Вывод списка в целом
print(m)
# Вывод списка поэлементно
for i in range(len(m)):
    print(m[i],end=' ')
