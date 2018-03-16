from tkinter import *

from algo.methods import predict_emotion

xx=0
umsg=[]
bmsg=[]

class UserBubble:
	def __init__(self,master,content):
		global xx
		global umsg
		global bmsg
		umsg.append(content)
		self.l1=Label(master,text="Me:",anchor="w",fg="red")
		self.l1.place(x=xx,y=0)
		self.l1.pack(fill="x")
		self.l2=Label(master,text=content,anchor="w")
		self.l2.place(x=xx+10,y=0)
		self.l2.pack(fill="x")
	#	self.l3=Label(master,text="",anchor="w",bg="red")
	#	self.l3.place(x=xx,y=0)
	#	self.l3.pack(fill="x")
		xx+=20
		b=BotBubble(master)

class BotBubble:
	def __init__(self,master):
		global xx
		global umsg
		global bmsg
		self.content=self.recommend()
		bmsg.append(self.content)
		self.l1=Label(master,text="Bot:",anchor="w",fg="blue")
		self.l1.place(x=xx,y=0)
		self.l1.pack(fill="x")
		self.l2=Label(master,text=self.content,anchor="w")
		self.l2.place(x=xx+10,y=0)
		self.l2.pack(fill="x")
	#	self.l3=Label(master,text="",anchor="w",bg="blue")
	#	self.l3.place(x=xx,y=0)
	#	self.l3.pack(fill="x")
		xx+=20

	def recommend (self):
		return predict_emotion()

'''master=Tk()
a=UserBubble(master,"input")
b=BotBubble(master,"answer")
master.minsize(width=600, height=600)
master.maxsize(width=600, height=600)
print(umsg,bmsg)
master.mainloop()'''
