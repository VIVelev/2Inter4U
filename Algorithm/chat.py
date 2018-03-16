import tkinter
from tkinter import *
from engine import *

ward = None
class Chat :
    def __init__(self,master) :
        self.master = master
        self.master.title("Chat")
        self.c=Canvas(master,borderwidth=0,background="#ffffff",width=600,height=500)
        self.frame=Frame(self.c,background="#ffffff")
        self.sc=Scrollbar(master,orient="vertical",command=self.c.yview)
        self.c.configure(yscrollcommand=self.sc.set)
        self.sc.pack(side="right",fill="y")
        self.c.pack(side="left",fill="both",expand=True)
        self.c.create_window((4,4),window=self.frame,anchor="nw")
        self.frame.bind("<Configure>",lambda event,canvas=self.c: self.onConfig())
        self.content = StringVar()
        self.content.set("")
        self.text_box = Entry(self.master, textvar=self.content , width = 400)
        self.text_box.bind("<Return>", self.submit)
        self.text_box.pack( side = tkinter.BOTTOM, padx = 100 , pady = 40)

    def submit(self,event = None):
        global ward
        ward = self.content.get()
        self.content.set("")
        a=UserBubble(self.frame,ward)

    def onConfig (self):
        self.c.configure(scrollregion=self.c.bbox("all"))


def main():
    master = Tk()
    master.minsize(width = 600,height = 700)
    master.maxsize(width = 600*2, height = 700*2)
    a = Chat(master)
    master.mainloop()

main()
