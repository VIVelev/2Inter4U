from flask import Flask, render_template, request
from models.nlp import preprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    X = preprocess(userText)
    print(X)
    return "Hello"

if __name__ == "__main__":
    app.run()
