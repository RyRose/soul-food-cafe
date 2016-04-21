from flask import Flask, flash, abort, session, render_template, redirect, request, url_for
app = Flask(__name__)

@app.route("/")
def index():
    session.clear()
    return render_template("index.html", page_title="Lorem")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    flash("what!")
    if request.method == "GET":
        return render_template("login.html", page_title="Login")

    elif request.method == "POST":
        # TODO: Check with database if user is in it.

        username = request.form['username']
        password = request.form['password']

        if username == password == 'admin':
            session['username'] = username
            return redirect(url_for('donations'))
        else:
            return render_template("login.html", page_title="Login", invalid=True)
    else:
        return render_template("login.html", page_title="Login")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        # TODO: Add donator to database. Possibly setup email confirmation.
        return redirect(url_for('login'))
    else:
        return render_template("register.html", page_title="Register")

@app.route("/donations")
def donations():
    if 'username' in session:
        return render_template("donations.html", page_title="Donations", name=session['username'])
    else:
        abort(418)
