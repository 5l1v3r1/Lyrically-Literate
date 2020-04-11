# OPERATION GET RED OCTOBERS 
import git
import hmac
import hashlib
import json
from flask import Flask, render_template, request, abort, redirect
from flask.json import jsonify
from utilites.lyrics import get_lyrics

app = Flask(__name__)


## GITHUB PULL WEBHOOK
def is_valid_signature(x_hub_signature, data, private_key):
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)


@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        abort_code = 418
        # Do initial validations on required headers
        if 'X-Github-Event' not in request.headers:
            abort(abort_code)
        if 'X-Github-Delivery' not in request.headers:
            abort(abort_code)
        if 'X-Hub-Signature' not in request.headers:
            abort(abort_code)
        if not request.is_json:
            abort(abort_code)
        if 'User-Agent' not in request.headers:
            abort(abort_code)
        ua = request.headers.get('User-Agent')
        if not ua.startswith('GitHub-Hookshot/'):
            abort(abort_code)

        event = request.headers.get('X-GitHub-Event')
        if event == "ping":
            return json.dumps({'msg': 'Hi!'})
        if event != "push":
            return json.dumps({'msg': "Wrong event type"})

        x_hub_signature = request.headers.get('X-Hub-Signature')
        if not is_valid_signature(x_hub_signature, request.data, "Mantini88"):
            print('Deploy signature failed: {sig}'.format(sig=x_hub_signature))
            abort(418)
        g = git.Git('Lyrically-Literate/')
        g.pull('launch','master')
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


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

