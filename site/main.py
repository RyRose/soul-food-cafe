import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash

app = Flask(__name__)
app.config.from_envvar('DB.ini', silent=True)
app.debug = True
app.secret_key = b'\x90\xef\xf4\x0f\x19P\xf9\xaa\x84D\t\x84\xdc\x19K\x87\xbe\xddZQ\x15\x1654'

@app.route("/")
def index():
    return render_template("index.html", page_title="Lorem")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html", page_title="Login")

    elif request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('donations'))
    else:
        return render_template("login.html", page_title="Login")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        return redirect(url_for('login'))
    else:
        return render_template("register.html", page_title="Register")

@app.route("/donations")
def donations():
    return render_template("donations.html", page_title="Donations")

if __name__ == "__main__":
    app.run()
