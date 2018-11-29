import random as rnd
import wikipedia

from dojo.linear import LinearRegression

from models.main import (
    get_named_entities,
    get_nouns,
    summarize_article,
    get_sentiment,

    log,
)


class ResPage:
    def __init__(self, title='', summary='', link=''):
        self.title = title
        self.summary = summary
        self.link = link

class Bot:
    def __init__(self, name):
        self.name = name

        self.pages_score = {}
        self.recommender_system = LinearRegression()
        self.prev_page = None
    
    def calc_page_score(self, page2analyze):
        wiki_pages = [wikipedia.page(title) for title in self.pages_score.keys()]
        X = [
            [len(get_named_entities(page.content)), len(get_nouns(page.content))] for page in wiki_pages
        ]
        y = self.pages_score.values()

        self.recommender_system.fit(X, y)
        return self.recommender_system.predict(
            [len(get_named_entities(page2analyze.content)),
            len(get_nouns(page2analyze.content))]
        )

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
        self.pages_score[self.prev_page.title] = sentiment

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
