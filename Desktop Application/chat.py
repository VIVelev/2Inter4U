import tkinter
from tkinter import *
def chat():
    master=tkinter.Tk()
    master.title("Chat")
    fr=tkinter.Frame(master)
    msg=tkinter.StringVar()
    msg.set("Type here")
    sc=tkinter.Scrollbar(fr)
    msglist=tkinter.Listbox(fr, height=15, width=50, yscrollcommand=sc.set)
    sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msglist.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msglist.pack()
    fr.pack()

    inputfield=tkinter.Entry(master, textvariable=msg)
    inputfield.bind("<Return>", lambda: None)
    inputfield.pack()
    logo = PhotoImage(file="send.pgm")
    send = tkinter.Button(master, image = logo, command= lambda : None, justify = RIGHT)
    send.pack(side = RIGHT)
    master.mainloop()
chat()
