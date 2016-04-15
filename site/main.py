import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash

app = Flask(__name__)
app.config.from_envvar('DB.ini', silent=True)
app.debug = app.config['DEBUG']

@app.route("/index")
@app.route("/")
def display_index():
    return render_template("index.html", page_title="Lorem")

@app.route("/login")
def display_login():
    return render_template("login.html", page_title="Login")

@app.route("/register")
def display_register():
    return render_template("register.html", page_title="Register")

@app.route("/donations")
def display_donations():
    return render_template("donations.html", page_title="Donations")

if __name__ == "__main__":
    app.run()
