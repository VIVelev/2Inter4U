from flask import Flask, render_template, request, redirect
from bot import Bot


app = Flask(__name__)
victor = Bot("Victor")

@app.route("/")
def index():
    victor.feedback(request.args.get("msg"))
    return render_template("index.html")

@app.route("/recommendation")
def get_bot_recommendation():
    page = victor.recommend_page(request.args.get("msg"))
    if not page:
        return redirect("/")
    return render_template("recommendation.html", page=page)

if __name__ == "__main__":
    app.run()
