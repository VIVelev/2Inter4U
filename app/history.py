import tkinter as tk

class History(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.canvas = tk.Canvas(master, borderwidth=0)
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.string = 'what the bot said'
        self.nums = ['link1', 'link2', 'link3', 'link4', 'link5']
        self.labels=[] #creates an empty list for your labels
        for x in  self.nums: #iterates over your nums
            self.jk = self.string + x
            self.label = tk.Label(master,text=self.jk) #set your text
            self.label.pack(pady = 80)
            self.labels.append(self.label) #appends the label to the list for further use
        '''self.populate()

    def populate(self):
        #Put in some fake data
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=4, )'''

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

master=tk.Tk()
History(master).pack(side="top", fill="both", expand=True)
master.minsize(width = 600,height = 700)
master.maxsize(width = 600, height = 700)
master.mainloop()
