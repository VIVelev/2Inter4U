from flask import Flask, render_template, request
from models.nlp import get_named_entities, get_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    named_ents = get_named_entities(userText)
    return str(named_ents)

if __name__ == "__main__":
    app.run()
