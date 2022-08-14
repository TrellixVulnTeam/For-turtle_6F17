from tkinter import *
from random import *
 
def печать(event):
     print ("Прежде чем о чем-то мечтать — подумай, а вдруг сбудется.")
              
tk = Tk()
tk.title("Привет, Мир! Ты как?")
tk.geometry('400x200') 

but = Button(tk)
but["text"] = "Печать"       # Такая надпись на кнопке
but.bind("<Button-Для уроков (составитель тестов)>",печать)# выводим кнопку и при нажатии на нее
                             # выполнять функцию печать ()
 
but.pack()
tk.mainloop() 
