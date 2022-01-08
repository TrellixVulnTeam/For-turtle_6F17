from tkinter import *
import math
# ---------------- Вывод окна и заголовка --------------------
tk=Tk()
tk.title(" Шахматная доска ") # заголовок окна
#
canvas=Canvas(tk) # задаем холст
canvas["height"]=600; canvas["width"]=800
canvas["background"]="#eeeeff"; canvas["borderwidth"]=2
canvas.pack()
#------------------фунция рисования окна----------------------
def окно(x,y,a,h,col=""): # функция рисования окна
    canvas.create_rectangle(x,y,x+a,y+h,fill=col)
    canvas.create_line(x+a//2,y,x+a//2,y+h,fill="black")
#-----------------функция рисования дома---------------------- 
def дом(x1,y1,n,m,w,сol_w,col="sienna1"):  # 
    # x1,y1 - координаты верхнего левого угла дома, n,m - ширина и высота
    # w - кол-во окон в ряду, col - цвет стен, col_w - цвет окон

    canvas.create_rectangle(x1,y1,x1+n,y1+m,fill=col) # нарисовали стены
    ширина_окна = (n - 20) // w - 10 # ширина одного окна
    высота_окна = ширина_окна + 10       # считаем, что окно на 10 точек больше ширины
    окон = (m - 20) // (ширина_окна +20) # количество окон по вертикали
        
    x=x1+15; y = y1+15;              # определяем отступ окна от края
    for i in range(окон):
         for j in range(w):
              окно(x,y,ширина_окна,высота_окна,"LemonChiffon1")
              x += ширина_окна + 10
         y += высота_окна + 10
         x = x1 + 15
    canvas.create_polygon(x1,y1,x1+n//2,y1 - m//10,x1+n,y1,fill="orchid1",outline="black") #

# собственно тело программы: построение ОДНОГО дома         
x=250; y=200; n=200; m=200 # начальные данные
дом(x,y,n,m,8,"LemonChiffon1","sienna1")

tk.mainloop()# это что вроде "выполнять программу"...

