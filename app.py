# OPERATION GET RED OCTOBERS 

from flask import Flask, render_template, request, abort, redirect
from flask.json import jsonify


app = Flask(__name__)


## ALL URL ROUTES
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


@app.route('/search-results')
def search_results():
    pass


# ALL POST VARIABLE ROUTES
@app.route("/search", methods=['POST'])
def search_post():
    search = request.form['search']
    print(f"Search: {search}")
    return render_template("/html/lyrics.html")


@app.route("/lyrics", methods=['POST'])
def lyrics_post():
    search_type = request.form['type']
    search_term = request.form['search-term']
    print(f"Lyrics Search: {search_type}")
    return render_template("/html/lyrics.html")


@app.route("/search/<first>-<last>-<song>")
def search(first=None, last=None, song=None):
    print(f"First name: {first} | Last name: {last} | Song name: {song}")
    return render_template("/html/lyrics.html")


if __name__ == "__main__":
    app.run(debug=True)

