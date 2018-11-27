import wikipedia
from flask import Flask, render_template, request

from models.nlp import get_named_entities, summarize_article, get_sentiment
from models.logging import log

##############################
IS_BOT_TURN = 1
PREV_PAGE = None
LIKED_PAGES = []
DISLIKED_PAGES = []
##############################

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    global IS_BOT_TURN, PREV_PAGE
    userText = request.args.get("msg")

    if IS_BOT_TURN:
        search_string = ' '.join([ent[0] for ent in get_named_entities(userText)])
        if search_string == '':
            return "I did not get that, can you repeat."

        log("SEARCHING FOR:", search_string)

        page_titles = wikipedia.search(search_string)
        log("Founded articles:\n", page_titles)

        ### Choose the most appropriate page based on previous activity ###
        IS_BOT_TURN = not IS_BOT_TURN
        PREV_PAGE = wikipedia.page(page_titles[0])

        log("Summarizing...")
        return summarize_article(PREV_PAGE.summary) + "More info here: " + str(PREV_PAGE.url)

    else:
        IS_BOT_TURN = not IS_BOT_TURN

        sentiment = get_sentiment(userText)[0][1]
        log(userText, ":", sentiment)

        if sentiment > .5:
            LIKED_PAGES.append(PREV_PAGE)
        else:
            DISLIKED_PAGES.append(PREV_PAGE)
        
        return "Thanks for the feedback."

if __name__ == "__main__":
    app.run()
