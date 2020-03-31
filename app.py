# OPERATION GET RED OCTOBERS 

from flask import Flask, render_template, request, abort, redirect
from flask.json import jsonify


app = Flask(__name__)


@app.route("/")
def default():
    return render_template("/html/home.html")


if __name__ == "__main__":
    app.run(debug=True)

