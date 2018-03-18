from tkinter import *

from datetime import datetime
import re
import random

import pandas as pd
import wikipedia

# Sentiment algo
from main.methods import predict_emotion

# Natural Language Preprocessing
from nlp_utils.methods import (
	preprocess,
	summarize_article,
	named_entity_recognition
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
RECOMMENDED_ARTICLES = []
counter_liked = 0

POSITIVE = [
	"Nice to hear that from you! ;)\nIn what other topic are you interested?",
	"I am happy to hear that!\nTell something else you want to know about.",
	"Do you need something else?",
	"What else do you want to talk about?",
	"Cool. Anything else?",
	"Thanks.\nWhat more can we talk about?",
	"Anything else I can help with :D?",
	"Would you like to checkout something?",
	"Tell me something else you are interested in.",
	"In what else are you interested? :)"
]
NEGATIVE = [
	"Well, tell me another topic.\nI will try my best, I promise.",
	"I will get better if you chat with me more.",
	"Ohh, sorry.\nTell me something else you are into.",
	"Let me try find you something one more time.",
	"Sorry mate.\nAsk me something else.",
	"Would you like to checkout something?",
	"Tell another thing you want to learn about.",
	"Somethin else I can help with?",
	"Ahh, I missed again.\nPlease, try one more time.",
	"My mistake.\nTry something else."
]

umsg=[]
bmsg=[]
roww=0
isOk = False

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
			if type(self.content) is list:
				data = self.content
				self.content = data[0] + "\n\nYou may also want to check out these articles:\n"
				for article in data[1]:
					self.content += "\t* "+str(article)+"\n"
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



	def get_page(self, topics):
		global ALL_ARTICLES
		matches = wikipedia.search(topics[0])

		isSeen = True				
		idx = 0
		page = wikipedia.page(matches[idx])

		# code for skipping seen articles #

		# if len(ALL_ARTICLES) > 0:
		# 	while isSeen:
		# 		for article in ALL_ARTICLES:
		# 			if page.title != article["title"]:
		# 				isSeen = False
		# 				break
		# 		if isSeen:
		# 			idx+=1
		# 			page = wikipedia.page(matches[idx])
		# else:
		# 	pass

		return page

	def recommend(self):
		global DATASET
		global ALL_ARTICLES
		global RECOMMENDED_ARTICLES
		global counter_liked		

		global POSITIVE
		global NEGATIVE	

		global umsg
		global bmsg
		global isOk

		topics = named_entity_recognition(umsg[-1])
		response = ""

		if len(topics) > 0:
			isOk = True
			print("\nRecognized topics: " + str(topics))

			if len(ALL_ARTICLES) < 3:
				page = self.get_page(topics)
				response = summarize_article(page.content)

				ALL_ARTICLES.append(
					{
						"title": page.title,
						"content": page.content,
						"date": datetime.now()
					}
				)

			else:
				like_this = []
				for i in range(counter_liked):
					like_this.append(create_liked_article(_id=i))

				body = {
    				"query": {
        				"more_like_this" : {
            				"fields": ["content"],
            				"like": like_this,
            				"min_term_freq": 1,
            				"max_query_terms": 12
        				}
   				 	}
				}

				res = es.search(index=INDEX_NAME, doc_type="article", body=body)
				print("\n------------> Got %d Hits <------------" % res['hits']['total'])
				hits = res["hits"]["hits"]
				
				if len(RECOMMENDED_ARTICLES) == 0:
					l = random.randint(0, len(hits)-1)
					h = random.randint(l+1, len(hits)-1)
					for hit in hits[l:h]:
						RECOMMENDED_ARTICLES.append(hit["_source"]["title"])


				page = self.get_page(topics)
				response = summarize_article(page.content)

				ALL_ARTICLES.append(
					{
						"title": page.title,
						"content": page.content,
						"date": datetime.now()
					}
				)

				# rnd = 0 # random.randint(0, len(hits)-1)
				# response = summarize_article(hits[rnd]["_source"]["content"])

				# ALL_ARTICLES.append(
				# 	{
				# 		"title": hits[rnd]["_source"]["title"],
				# 		"content": hits[rnd]["_source"]["content"],
				# 		"date": hits[rnd]["_source"]["date"]
				# 	}
				# )


		elif len(bmsg) > 1 and isOk:
			X_tf = preprocess(umsg[-1])
			label = predict_emotion(X_tf)

			DATASET = DATASET.append(
				pd.DataFrame(
					[[bmsg[-1], label]],
					columns=["text", "label"]
				),
				ignore_index=True
			)
			print("\nDATASET" + str(DATASET))

			if label == "1":
				response = POSITIVE[random.randint(0, len(POSITIVE)-1)]

				liked_article = ALL_ARTICLES[-1]
				doc = {
					"title": liked_article["title"],
					"content": liked_article["content"],
					"date": liked_article["date"]
				}
				res = es.index(index=LIKED_ARTICLES_INDEX_NAME, doc_type="article", id=counter_liked, body=doc)
				counter_liked+=1

			else:
				response = NEGATIVE[random.randint(0, len(NEGATIVE)-1)]

			if RECOMMENDED_ARTICLES:
				response = [response, RECOMMENDED_ARTICLES]
				RECOMMENDED_ARTICLES = []

			isOk = False

		else:
			response = "Sorry, I did not uderstand that. :("
								
		return response
