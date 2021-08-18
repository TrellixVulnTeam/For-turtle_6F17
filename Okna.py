from simpletk import *
from tkinter.messagebox import askokcancel


def AskOnExit(sender):
    if askokcancel("Подтверждение", "Вы действительно хотите выйти из программы?"):
        app.destroy()


app = TApplication("Первая форма")
app.size = (500, 200)
app.resizable = (True, False)
app.onCloseQuery = AskOnExit
app.Run()





