from tkinter import *

import pandas as pd
import re
import wikipedia

from main.methods import predict_emotion

from nlp_utils.methods import (
	preprocess,
	summarize_article,
	summarize_categories,
	named_entity_recognition,
)

# Recommendation system
from elastic_search.main import (
    es,

    isLoaded,
	INDEX_NAME,
    N_WIKI_PAGES,
    init_index,

    init_liked_articles_index,
    create_liked_article,
    LIKED_ARTICLES_INDEX_NAME
)

init_index()
init_liked_articles_index()
#######################

DATASET = pd.DataFrame(columns=["text", "label"])
ALL_ARTICLES = []

umsg=[]
bmsg=[]
isOk = False
counter = 0

roww=0

class UserBubble:
	def __init__(self,frame,content):
		global roww
		global umsg
		global bmsg
		umsg.append(content)
		self.l1=Label(frame,text="Me:",anchor="w",fg="red",width=1000, bg = "wheat3",font=("CourierNew",12))
		self.l1.pack(fill="x")
		roww+=1
		self.l2=Label(frame,text=content,anchor="w", bg = "wheat3",font=("CourierNew",12))
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
		self.l1=Label(frame,text="Bot:",anchor="w",fg="blue",bg="wheat3",font=("CourierNew",12))
		self.l1.pack(fill="x")
		roww+=1
		self.l2=Label(frame,text=self.content,justify=LEFT,anchor="w",bg="wheat3",width=500,wraplength=580,font=("CourierNew",12))
		self.l2.pack(fill="x")
		roww+=1


	def recommend(self):
		global DATASET

		global umsg
		global bmsg
		global isOk		

		topics = named_entity_recognition(umsg[-1])
		response = ""

		if len(topics) > 0:
			isOk = True
			print("\nRecognized topics: " + str(topics))

			if len(bmsg) == 1:
				page = wikipedia.page(wikipedia.search(topics[0])[0])
				article = page.content
				response = summarize_article(article)
				ALL_ARTICLES.append(
					create_liked_article(_id=counter, _type="article", INDEX_NAME=LIKED_ARTICLES_INDEX_NAME)
					)
				counter+=1

			else:
				# liked_article = ""
				# for i in range(len(DATASET)):
				# 	if DATASET.iloc[i]["label"] == "1":
				# 		liked_article = DATASET.iloc[i]["text"]

				body = {
    				"query": {
        				"more_like_this" : {
            				"fields" : ["title"],
            				"like" : topics[0],
            				"min_term_freq" : 1,
            				"max_query_terms" : 12
        				}
   				 	}
				}
				res = es.search(index=INDEX_NAME, body=body)
				print("\nGot %d Hits:" % res['hits']['total'])
				print(res)


		elif len(bmsg) > 1 and isOk:
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

			if label == "1":
				response = "Nice to hear that from you! ;)\nIn what other topic are you interested?"
				liked_article = ALL_ARTICLES[-1]
				res = es.index(index=liked_article["_index"], doc_type=liked_article["_type"], id=liked_article["_id"])
			else:
				response = "In what other topic are you interested?"

			isOk = False
		
		else:
			response = "Sorry, I did not uderstand that. :("

		if len(DATASET) > 0:
			print("\nDATASET" + str(DATASET))
								
		return response
