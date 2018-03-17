from tkinter import *

from main.methods import predict_emotion
from nlp_utils.methods import (
	preprocess,
	summarize_article,
	named_entity_recognition
)

import wikipedia
import re

roww=0
umsg=[]
bmsg=[]

class UserBubble:
	def __init__(self,frame,content):
		global roww
		global umsg
		global bmsg
		umsg.append(content)
		self.l1=Label(frame,text="Me:",anchor="w",fg="red",width=1000)#.grid(row=roww,column=0)
		self.l1.pack(fill="x")
		roww+=1
		self.l2=Label(frame,text=content,anchor="w")#.grid(row=roww,column=0)
		self.l2.pack(fill="x")
		roww+=1
		b=BotBubble(frame)

class BotBubble:
	def __init__(self,frame):
		global roww
		global umsg
		global bmsg
		self.content=self.recommend()
		bmsg.append(self.content)
		self.l1=Label(frame,text="Bot:",anchor="w",fg="blue")#.grid(row=roww,column=0)
		self.l1.pack(fill="x")
		roww+=1
		self.l2=Label(frame,text=self.content,justify=LEFT,anchor="w",width=500)#.grid(row=roww,column=0)
		self.l2.pack(fill="x")
		roww+=1


	def recommend(self):
		global umsg
		
		if named_entity_recognition(umsg[-1]):
			topics = named_entity_recognition(umsg[-1])
			print(topics)

			article = wikipedia.page(wikipedia.search(topics[0])[0]).content
			response = summarize_article(article)
			return response

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
