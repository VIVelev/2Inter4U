from tkinter import *

root = Tk()
root.geometry('1000x500')

logo = PhotoImage(file="../img/ourteam.gif")
background=Label(root, image=logo).place(x=0,y=0,relwidth=1, relheight=1)




root.mainloop()
