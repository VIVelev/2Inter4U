import random as rnd
import wikipedia

from models.nlp import get_named_entities, summarize_article, get_sentiment
from models.logging import log


class Bot:

    def __init__(self, name):
        self.name = name

        self.liked_pages = []
        self.disliked_pages = []
        self.prev_page = []

        self.awaiting_feedback = False
    
    def recommend(self, msg):
        search_string = ' '.join([ent[0] for ent in get_named_entities(msg)])
        if search_string == '':
            return "What would you like to know about?"

        log("SEARCHING FOR:", search_string)

        page_titles = wikipedia.search(search_string)
        log("Founded articles:\n", page_titles)

        ### Choose the most appropriate page based on previous activity ###
        self.awaiting_feedback = not self.awaiting_feedback

        log("Loading...")
        loaded = False
        while not loaded:
            try:
                self.prev_page = wikipedia.page(rnd.choice(page_titles))
                loaded = True
            except wikipedia.exceptions.DisambiguationError:
                pass      

        print(self.prev_page.categories)

        log("Summarizing...")
        return summarize_article(self.prev_page.summary) + "More info here: " + str(self.prev_page.url)

    def feedback(self, msg):
        self.awaiting_feedback = not self.awaiting_feedback
        
        sentiment = get_sentiment(msg)[0][1]
        log(msg, ":", sentiment)

        if sentiment > .5:
            self.liked_pages.append(self.prev_page)
        else:
            self.disliked_pages.append(self.prev_page)
        
        return "Thanks for the feedback."

    def response(self, msg):
        if self.awaiting_feedback:
            return self.feedback(msg)
        else:
            return self.recommend(msg)
