from tkinter import *

xx=0

class UserBubble:
	def __init__(self,master,content):
		global xx
		self.l1=Label(master,text="Me:",anchor="w",fg="red")
		self.l1.place(x=xx,y=0)
		xx+=10
		self.l1.pack(fill="x")
		self.l=Label(master,text=content,anchor="w")
		self.l.place(x=xx,y=0)
		xx+=10
		self.l.pack(fill="x")

master=Tk()
a=UserBubble(master,"input")
master.minsize(width=600, height=600)
master.maxsize(width=600, height=600)
master.mainloop()
