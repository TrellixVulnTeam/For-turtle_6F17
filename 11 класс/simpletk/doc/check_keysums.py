import tkinter as tk

def __keyPress(event):
  print("Key Press Event:")
  print("  event.char:", event.char)
  print("  event.keysym:", event.keysym)
  print("  event.keycode:", event.keycode)
  print("  event.keysym_num:", event.keysym_num)

def __keyRelease(event):
  print("Key Release Event:")
  print("  event.char:", event.char)
  print("  event.keysym:", event.keysym)
  print("  event.keycode:", event.keycode)
  print("  event.keysym_num:", event.keysym_num)

def main():
  __master = tk.Tk()
  __master.bind("<KeyPress>", __keyPress)
  __master.bind("<KeyRelease>", __keyRelease)
  tk.mainloop()

main()