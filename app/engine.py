from tkinter import *

import pandas as pd
import re

from main.methods import predict_emotion

from nlp_utils.methods import (
	preprocess,
	summarize_article,
	summarize_categories,
	named_entity_recognition,
)

# Recommendation system
from elastic_search.main import init_index
es = init_index()
#######################

DATASET = pd.DataFrame(columns=["text", "label"])
# WIKI_TAGS = pd.DataFrame(columns=["text", "label"])
WIKI_PAGES = []

umsg=[]
bmsg=[]

roww=0

class UserBubble:
	def __init__(self,frame,content):
		global roww
		global umsg
		global bmsg
		umsg.append(content)
		self.l1=Label(frame,text="Me:",anchor="w",fg="red",width=1000, bg = "wheat3")#.grid(row=roww,column=0)
		self.l1.pack(fill="x")
		roww+=1
		self.l2=Label(frame,text=content,anchor="w", bg = "wheat3")#.grid(row=roww,column=0)
		self.l2.pack(fill="x")
		roww+=1
		b=BotBubble(frame)

class BotBubble:
	def __init__(self,frame, content=None):
		global roww
		global umsg
		global bmsg

		if content == None:
			self.content=self.recommend()
		else:
			self.content = content

		bmsg.append(self.content)
		# self.f=open("./history.txt", "a")
		# self.f.write(str(self.content)+"\n")
		# self.f.close()
		self.l1=Label(frame,text="Bot:",anchor="w",fg="blue",bg="wheat3")#.grid(row=roww,column=0)
		self.l1.pack(fill="x")
		roww+=1
		self.l2=Label(frame,text=self.content,justify=LEFT,anchor="w",bg="wheat3",width=500,wraplength=580)#.grid(row=roww,column=0)
		self.l2.pack(fill="x")
		roww+=1


	def recommend(self):
		global DATASET
		# global WIKI_TAGS
		global WIKI_PAGES

		global umsg
		global bmsg
		
		topics = named_entity_recognition(umsg[-1])
		response = ""

		if len(topics) > 0:
			print("\nRecognized topics: " + str(topics))

			if len(WIKI_PAGES) == 0:
				page = wikipedia.page(wikipedia.search(topics[0])[0])
				WIKI_PAGES.append(page)
				article = page.content
				response = summarize_article(article)
				
			else:
				page = wikipedia.page(wikipedia.search(topics[0])[0])
				WIKI_PAGES.append(page)
				article = page.content
				response = summarize_article(article)

		elif len(bmsg) > 1:
			last_umsg = umsg[-1]

			X_tf = preprocess(last_umsg)
			label = predict_emotion(X_tf)

			DATASET = DATASET.append(
				pd.DataFrame(
					[[bmsg[-1], label]],
					columns=["text", "label"]
				),
				ignore_index=True
			)

			# last_article_categories = ". ".join(WIKI_PAGES[-1].categories)
			# print(last_article_categories)

			# WIKI_TAGS = WIKI_TAGS.append(
			# 	pd.DataFrame(
			# 		[
			# 			[
			# 				summarize_categories(last_article_categories),
			# 				label
			# 			]
			# 		],
			# 		columns=["text", "label"]
			# 	),
			# 	ignore_index=True
			# )
		
		else:
			response = "Sorry, I did not uderstand that. :("

		if len(DATASET) > 0:
			print("\nDATASET\n" + str(DATASET))	
		# if len(WIKI_TAGS) > 0:
		# 	print("\nWIKI_TAGS" + str(WIKI_TAGS))							
		return response
