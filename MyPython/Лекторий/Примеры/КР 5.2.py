print("Шифр цезаря")
строка = input("Введите строку ")
сдвиг = int(input("Введите сдвиг "))
ключ="1234567890АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+!№;:?*()_+"

ключ_сдвиг=""
шифр=""
дешифр=""

if сдвиг > 0:
    for i in range(len(ключ)): # создание строки для шифрования 
        if (i + сдвиг)> (len(ключ)-1):
            ключ_сдвиг += ключ[i+сдвиг-(len(ключ))]
        else:
            ключ_сдвиг += ключ[i+сдвиг]
elif сдвиг < 0:
    for i in range(len(ключ)): # создание строки для шифрования 
        if (i + сдвиг) < 0:
            ключ_сдвиг += ключ[len(ключ)-i+сдвиг]
        else:
            ключ_сдвиг += ключ[i+сдвиг]
elif сдвиг == 0:
    ключ_сдвиг = ключ
    

            
for i in range(len(строка)): #шифрование Цезаря
    шифр += ключ_сдвиг[ключ.index(строка[i])]

print (шифр)

for i in range(len(шифр)): #шифрование Цезаря
    дешифр += ключ[ключ_сдвиг.index(шифр[i])]

print (дешифр)
