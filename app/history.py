from tkinter import *


class History :
    def __init__(self,master) :
        self.master = master
        self.string = 'sumaraiza ot bota '
        self.nums = ['link1', 'link2', 'link3']
        self.labels=[]
        self.c=Canvas(master,borderwidth=0)
        self.frame=Frame(self.c)
        self.sc=Scrollbar(master,orient="vertical",command=self.c.yview)
        self.c.configure(yscrollcommand=self.sc.set)
        self.sc.pack(side="right",fill="y")
        self.c.pack(side="left",fill="both",expand=True, pady=(0,80))
        self.c.create_window((4,4),window=self.frame,anchor="nw")
        for x in self.nums:
            self.jk = self.string + x
            self.label = Label(master,text=self.jk)
            self.label.pack(pady = 15)
            self.labels.append(self.label)
    def onConfig (self):
        self.c.configure(scrollregion=self.c.bbox("all"))



master = Tk()
h = History(master)
master.minsize(width = 600,height = 600)
master.maxsize(width = 600, height = 600)
master.mainloop()
