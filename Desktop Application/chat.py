import tkinter
from tkinter import *
from engine import *
ward = None
class Chat :
    def __init__(self,master) :
        self.master = master
        #fr = Frame(self.master)
        self.master.title("Chat")
        self.content = StringVar()
        self.content.set("Click Enter to send ")
        self.text_box = Entry(self.master, textvar=self.content , width = 400)
        #self.text_box.place(x = 450, y = 600)
        self.text_box.bind("<Return>", self.submit)
        self.text_box.pack( side = tkinter.BOTTOM, padx = 100 , pady = 40)
        self.send_button = Button(self.master, text = "send", command = lambda : None)
        self.send_button.place(x = 450, y =600)
        #self.send_button.pack()

    def submit(self,event = None):
        global ward
        ward = self.content.get()
        self.content.set("")
        a=UserBubble(self.master,ward)


master = Tk()
#a = UserBubble(master, "sami e mnogo gotin kappa")
#b = BotBubble(master, "viki e mnogo lud")
master.minsize(width = 600,height = 700)
master.maxsize(width = 600, height = 700)
a = Chat(master)
master.mainloop()
