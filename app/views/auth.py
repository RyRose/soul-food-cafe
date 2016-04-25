from flask import Blueprint, flash, abort, session, render_template, redirect, request, url_for
from app.forms import LoginForm

auth = Blueprint('auth', __name__)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    is_invalid = False
    if form.validate_on_submit():
        username = form.data["username"]
        password = form.data["password"]

        # TODO: Check with database if user is in it.
        print(username, password)
        if username == password == 'admin':
            session['username'] = username
            return redirect(url_for('donation.donations'))
        else:
            is_invalid = True

    return render_template("login.html", page_title="Login", invalid=is_invalid, form=form)

# TODO: Setup changing of login to logout whenever login state changes
@auth.route("/logout")
def logout():
    session.pop('username')
    return redirect(url_for("index"))

@auth.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        # TODO: Add donator to database. Possibly setup email confirmation.
        return redirect(url_for('login'))
    else:
        return render_template("register.html", page_title="Register")
