from flask import Blueprint, flash, abort, session, render_template, redirect, request, url_for
from app import db
from app.forms import LoginForm, RegisterForm
from app.forms import flash_errors
from app.models import Donor, Admin

auth = Blueprint('auth', __name__)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        donor = Donor.query.filter_by(username=username).first()
        if donor is not None:
            if donor.check_password(form.data["password"]):
                session["username"] = username
                return redirect(url_for("donation.donations"))
        else:
            flash("Username does not exist. Please try again with a different username/password.")
    else:
        flash_errors(form)

    return render_template("login.html", page_title="Login", form=form)

@auth.route("/admin/login", methods = ['GET', 'POST'])
def admin_login():
    if "is_admin" in session and session["is_admin"]:
        return redirect(url_for("donation.donations"))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        admin = Admin.query.filter_by(username=username).first()
        if admin is not None:
            if admin.check_password(form.data["password"]):
                session["username"] = username
                session["is_admin"] = True
                return redirect(url_for("donation.donations"))
        else:
            flash("Username does not exist. Please try again with a different username/password.")
    else:
        flash_errors(form)

    return render_template("login.html", page_title="Administrative Login", form=form, admin=True)


@auth.route("/logout")
def logout():
    session.pop('username')
    if "is_admin" in session:
        session.pop("is_admin")
        flash("You just logged out")
    return redirect(url_for("index"))

@auth.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.data["email"]
        username = form.data["username"]
        password = form.data["password"]

        if Donor.query.filter_by(username=username).first() == None:
            donor = Donor(email, username, password)
            db.session.add(donor)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash("Username already exists. Please choose a different username")
    else:
        flash_errors(form)

    return render_template("register.html", page_title="Register", form=form)
