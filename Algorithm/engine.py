from tkinter import *

from main.methods import predict_emotion
from nlp_utils.methods import preprocess, summarize_article, named_entity_recognition

import wikipedia

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
		global umsg
		
		if named_entity_recognition(umsg[-1]):
			topics = named_entity_recognition(umsg[-1])
			return summarize_article(wikipedia.page(topics[0]).content)

		else:
			last_msg = umsg[-1]
			X_tf = preprocess(last_msg)
			return predict_emotion(X_tf)
	


'''master=Tk()
a=UserBubble(master,"input")
b=BotBubble(master,"answer")
master.minsize(width=600, height=600)
master.maxsize(width=600, height=600)
print(umsg,bmsg)
master.mainloop()'''
