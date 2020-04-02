# OPERATION GET RED OCTOBERS 

from flask import Flask, render_template, request, abort, redirect
from flask.json import jsonify


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/html/home.html")


@app.route("/featured")
def featured():
    return render_template("/html/home.html")


@app.route("/lyrics")
def lyrics():
    return render_template("/html/lyrics.html")


@app.route("/news")
def news():
    return render_template("/html/news.html")


@app.route("/about")
def about():
    return render_template("/html/about.html")


@app.route("/shop")
def shop():
    return render_template("/html/shop.html")


if __name__ == "__main__":
    app.run(debug=True)

