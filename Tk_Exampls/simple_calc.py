import tkinter as tk

font_tyle  = 'Arial, 20'

window = tk.Tk()
frame1 = tk.Frame(window).pack()
frame2 = tk.Frame(window).pack()
frame3 = tk.Frame(window).pack()
frame4 = tk.Frame(window).pack()
frame5 = tk.Frame(window).pack()

ans = tk.Entry(frame1, width=10, font=font_tyle)
ans.pack(padx=5, pady=5)

buttons = []
var = tk.IntVar()



window.mainloop()
