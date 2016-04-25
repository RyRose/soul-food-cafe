from flask import Flask, flash, abort, session, render_template, redirect, request, url_for

from .views.auth import auth
from .views.donations import donation

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(donation)

@app.route("/")
def index():
    return render_template("index.html", page_title="Lorem")