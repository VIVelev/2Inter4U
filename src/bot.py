import random as rnd
import wikipedia

from models.nlp import (
    get_named_entities,
    get_nouns,
    summarize_article,
    get_sentiment,
)
from models.logging import log


class ResPage:
    def __init__(self, title='', summary='', link=''):
        self.title = title
        self.summary = summary
        self.link = link

class Bot:
    def __init__(self, name):
        self.name = name

        self.pages_stats = {}
        self.prev_page = None
    
    def get_search_string(self, msg):
        search_string = ' '.join([ent[0] for ent in get_named_entities(msg)])
        search_string += ' '
        search_string += ' '.join([noun for noun in get_nouns(msg)])

        return search_string

    def recommend_page(self, msg):
        search_string = self.get_search_string(msg)
        if search_string == ' ':
            return False
        log("SEARCHING FOR:", search_string)

        page_titles = wikipedia.search(search_string)
        log("Founded articles:\n", page_titles)

        ### Choose the most appropriate page based on previous activity ###
        log("Loading...")
        loaded = False
        while not loaded:
            try:
                self.prev_page = wikipedia.page(rnd.choice(page_titles))
                loaded = True
            except wikipedia.exceptions.DisambiguationError:
                pass

        log("Summarizing...")
        return ResPage(
            self.prev_page.title,
            summarize_article(self.prev_page.content),
            self.prev_page.url
        )
        
    def feedback(self, msg):
        if msg is None:
            return False

        sentiment = get_sentiment(msg)[0][1]
        log(msg, ":", sentiment)
        self.pages_stats[self.prev_page.title] = sentiment

        res = "Thanks for the feedback. I recorder that you "
        if sentiment < .5:
            res += "do not "
        return res + f"like the page: {self.prev_page.title}"

    def response(self, msg):
        if self.get_search_string(msg) == ' ':
            if self.prev_page is not None:
                return self.feedback(msg)
            else:
                return "What would you like to know about?"
        else:
            return self.recommend_page(msg)
