from tkinter import *


class History :
    def __init__(self,master) :
        self.master = master
        frame = Frame(self)
        self.string = 'sumaraiza ot bota '
        self.nums = ['link1', 'link2', 'link3', 'link4', 'link5', 'link6']
        self.labels=[]
        '''self.c=Canvas(master,borderwidth=0)
        self.frame=Frame(self.c)
        self.sc=Scrollbar(master,orient="vertical",command=self.c.yview)
        self.c.configure(yscrollcommand=self.sc.set)
        self.sc.pack(side="right",fill="y")
        self.c.pack(side="left",fill="both",expand=True, pady=(0,80))
        self.c.create_window((4,4),window=self.frame,anchor="nw")'''
        self.canvas = Canvas(master, borderwidhth=0)
        self.frame = Frame(self.canvas)
        self.vsb = Scrollbar(master, orient = "vertical", command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.vsb.set)

        self.vsb.pack(side = "right", fill = "both", expand = True)
        self.canvas.create_window((4,4), window = self.frme, anchor = "nw", tags = "self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.populate()

        for x in self.nums:
            self.jk = self.string + x
            self.label = Label(frame,text=self.jk, anchor="w",width=1000)
            self.label.pack(pady = 50, fill="x")
            self.labels.append(self.label)

    def populate(self) :
        for row in range (100):
            tk.Label(self.frame, text = "%s" % row, width = 3, borderwidht = "1", relief = "solid").grid(row = row , column = 0)
            t = "what %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self,event):self.canvas.configure(scrollregion=self.canvas.bbox("all"))





    def onConfig (self):
        self.c.configure(scrollregion=self.c.bbox("all"))



master = Tk()
h = History(master)
master.minsize(width = 600,height = 600)
master.maxsize(width = 600, height = 600)
master.mainloop()
