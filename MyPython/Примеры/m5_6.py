from tkinter import *
import math
#
tk=Tk() # Вывод окна
tk.title(" Шахматная доска ") # заголовок окна
#
canvas=Canvas(tk);
canvas["height"]=360
canvas["width"]=480
canvas["background"]="#eeeeff"
canvas["borderwidth"]=2
canvas.pack()
#
canvas.create_text(130, 25, text="Рисуем примитивы в цикле\nна холсте",
                            font=("Times New Roman", 14), anchor="w",
                            justify=CENTER, fill="DarkSlateBlue")
x=20; y=60; a=50
c = 1
while x < 450:
     if c % 2 == 0: col = "white"
     else: col = "black"
     c+=1
     canvas.create_rectangle(x,y,x+a,y+a,fill=col)
     x += 55 
tk.mainloop()# это что вроде "выполнять программу"...
