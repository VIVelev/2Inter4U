from flask import Flask, render_template, request
from Bot import Bot


app = Flask(__name__)
victor = Bot("Victor")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    return victor.response(request.args.get("msg"))

if __name__ == "__main__":
    app.run()
