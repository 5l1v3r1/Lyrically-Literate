# OPERATION GET RED OCTOBERS 

from flask import Flask, render_template, request, abort, redirect
from flask.json import jsonify
from utilites.lyrics import get_lyrics

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


@app.route('/search')
def search():
    return render_template("/html/lyrics.html")



# ALL POST VARIABLE ROUTES
## SEARCH BAR RESULTS ----> LYRCIS RESULTS PAGE + CLICK -----> CONTENT_PAGE

## SEARCH FROM BAR
@app.route("/search", methods=['POST'])
def search_post():
    search = request.form['search']
    print(f"Search: {search}")
    return render_template("/html/lyrics.html")


## SEARCH FROM LYRICS PAGE
@app.route("/lyrics", methods=['POST'])
def lyrics_post():
    search_type = request.form['type']
    search_term = request.form['search-term']
    print(f"Search Query: {search_type} | Term: {search_term}")
    lyrics_return = get_lyrics(search_term)
    return render_template("/html/lyrics.html", lyrics=lyrics_return)


## MAIN SEARCH URL -- ALL WILL BE REDIRECTED TO HERE -- ACTUAL CONTENT PAGE -- LYRCIS RESULTS HAS LINK TO GO HERE
@app.route("/search/<first>-<last>-<song>")
def search_manual(first=None, last=None, song=None):
    print(f"First name: {first} | Last name: {last} | Song name: {song}")
    return render_template("/html/content_page.html")


if __name__ == "__main__":
    app.run(debug=True)

