#жених=int(input("Введите возраст женха "))
#невеста=int(input("Введите возраст невесты "))
#
#if невеста==(жених//2+7):
#    print("Подходят они")
#else:
#    print("Не подходят")
#
#число=int(input("Введите число "))
#if (число//2)==0:
#    print("Число чётное")
#else:
#    print("Число нечётное")

from math import *
#x1=int(input("Введите первое число "))
#x2=int(input("Введите второе число "))
#x3=int(input("Введите третье число "))
#print ("Максимальное число", max(x1,x2,x3))

#from datetime import *
#aux=datetime.now().year
#print(aux)
#роджён=int(input("Введите год рождения "))
#if (aux - роджён) <0 or (aux - роджён)>150:
#    print("Error")
#else:
#    print("Вам",aux - роджён, "лет")
#
#print("Начало")
#for i in range(0,20,1):
#    print(i+1, "ФИО")
#print("Конец")
    
#num = int(input("Количество слогаемых "))
#summ = 0
#for i in range(num):
#    summ=summ+int(input(str(i+1)+"-е число = "))
#print ("Сумма = ", summ)

n = int(input("Количество точек "))
x= float(input("Координата Х точки 1"))
y= float(input("Кощрдината У точеи 1"))

a,b=x,y
m=sqrt(x*x+y*y)

for i in range(2,n+1):
    x= float(input("Координата Х "+str(i)+" точки "))
    y= float(input("Кощрдината У "+str(i)+" точки "))
    if m < sqrt(x*x+y*y):
        a,b=x,y
print("Координаты точки" ,a,b,sep=",")


        

