from flask import Flask, flash, abort, session, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

from .views.auth import auth
from .views.donations import donation

app.register_blueprint(auth)
app.register_blueprint(donation)

@app.route("/")
def index():
    return render_template("index.html", page_title="Lorem")

from app import models
