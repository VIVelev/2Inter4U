import tkinter
from tkinter import *
from engine import *
class Chat :
    def __init__(self,master) :
        self.master = master
        #fr = Frame(self.master)
        self.master.title("Chat")
        self.content = StringVar()
        self.content.set("Type your message here")
        self.text_box = Entry(self.master, textvar=self.content , width = 400)
        self.text_box.place(x = 450, y = 600)
        self.text_box.pack( side = tkinter.BOTTOM, padx = 100 , pady = 40)

master = Tk()
master.minsize(width = 600,height = 700)
master.maxsize(width = 600, height = 700)
a = Chat(master)
master.mainloop()
