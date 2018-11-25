import wikipedia
from flask import Flask, render_template, request

from models.nlp import get_named_entities, summarize_article, get_sentiment

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

        print('-'*100)
        print("SEARCHING FOR:", search_string)
        print()

        page_titles = wikipedia.search(search_string)
        print("Founded articles:\n")
        print(page_titles)
        print('-'*100)

        pages = []
        for title in page_titles:
            try:
                pages.append(wikipedia.page(title))
            except wikipedia.exceptions.DisambiguationError:
                return "Can you be more specific, please."

        ### Choose the most appropriate page based on previous activity ###
        IS_BOT_TURN = not IS_BOT_TURN
        PREV_PAGE = pages[0]
        return summarize_article(pages[0].content) + "More info here: " + str(pages[0].url)

    else:
        IS_BOT_TURN = not IS_BOT_TURN

        sentiment = get_sentiment(userText)[0][1]
        print('-'*100)
        print(userText, ":", sentiment)
        print('-'*100)

        if sentiment > .5:
            LIKED_PAGES.append(PREV_PAGE)
        else:
            DISLIKED_PAGES.append(PREV_PAGE)
        
        return "Thanks for the feedback."

if __name__ == "__main__":
    app.run()
