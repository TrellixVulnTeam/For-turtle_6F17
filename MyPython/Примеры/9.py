#замена символов в строке
def замена (строка,позиция,символ):
    return строка[:позиция]+симаол+строка[позиция+1:]

#предложение=input("Введите предложение")
#print(предложение.replace(" ","\n"))
#слова=предложение.split(" ")
#for i in слова :
#    print(i)
слово=input("Введите слово ")
for i in range(len(слово)):
    print(слово[i], end="\n")
print('*****************************')
for i in слово:
    print(i, end="\n")
