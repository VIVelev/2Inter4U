from tkinter import *


class History :
    def __init__(self,master) :
        self.master = master
        self.string = 'sumaraiza ot bota '
        self.nums = ['link1', 'link2', 'link3']
        self.labels=[]
        for x in self.nums:
            self.jk = self.string + x
            self.label = Label(master,text=self.jk)
            self.label.pack(pady = 15)
            self.labels.append(self.label)




master = Tk()
h = History(master)
master.minsize(width = 600,height = 600)
master.maxsize(width = 600, height = 600)
master.mainloop()
