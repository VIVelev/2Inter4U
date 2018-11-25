import wikipedia
from flask import Flask, render_template, request

from models.nlp import get_named_entities, summarize_article, get_sentiment


app = Flask(__name__)
IS_BOT_TURN = 1

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    global IS_BOT_TURN
    userText = request.args.get("msg")

    if IS_BOT_TURN:
        search_string = ' '.join([ent[0] for ent in get_named_entities(userText)])
        page_titles = wikipedia.search(search_string)
        pages = []
        for title in page_titles:
            try:
                pages.append(wikipedia.page(title))
            except wikipedia.exceptions.DisambiguationError:
                return "Can you be more specific, please."

        ### Choose the most appropriate page based on previous activity ###
        IS_BOT_TURN = not IS_BOT_TURN
        return summarize_article(pages[0].content)

    else:
        IS_BOT_TURN = not IS_BOT_TURN
        return str(get_sentiment(userText))

if __name__ == "__main__":
    app.run()
