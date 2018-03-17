import tkinter
from tkinter import *
from engine import *
import sys

ward = None
class Chat:
    def __init__(self, master) :
        self.master = master
        self.master.title("Chat")
        self.c=Canvas(master,borderwidth=0,background="wheat3")
        self.frame=Frame(self.c,background="blue")
        self.sc=Scrollbar(master,orient="vertical",command=self.c.yview)
        self.c.configure(yscrollcommand=self.sc.set)
        self.sc.pack(side="right",fill="y")
        self.c.pack(side="left",fill="both",expand=True, pady=(0,80))
        self.c.create_window((4,4),window=self.frame,anchor="nw")
        self.frame.bind("<Configure>",lambda event,canvas=self.c: self.onConfig())
        self.content = StringVar()
        self.content.set("")
        self.text_box = Entry(self.master, textvar=self.content,width=50)
        self.text_box.bind("<Return>", self.submit)
        self.text_box.place(x=50,y=650)

        self.welcome_msg = BotBubble(self.frame, content="What topic are you interested in?")
       # self.text_box.pack( side = tkinter.BOTTOM, padx = 100 , pady = 40)

    def submit(self,event = None):
        global ward
        ward = self.content.get()
        self.content.set("")
        a=UserBubble(self.frame,ward)

    def onConfig (self):
        self.c.configure(scrollregion=self.c.bbox("all"))


def main():
    try:
        if (str(sys.argv[1]) == "1"):
            master = Tk()
            master.minsize(width=600, height=700)
            master.maxsize(width=600, height=700)
            a = Chat(master)
            master["bg"] = "wheat3"
            master.mainloop()
    except:
        return

main()
