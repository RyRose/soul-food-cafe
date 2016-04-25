from flask import Blueprint, render_template, redirect, session, flash, url_for

donation = Blueprint('donation', __name__)

@donation.route("/donations")
def donations():
    if 'username' in session:
        # TODO: Add stuff from database
        return render_template("donations.html", page_title="Donations", name=session['username'])
    else:
        flash("Please login.")
        return redirect(url_for('auth.login'))
        
@donation.route("/donations/add", methods = ['GET', 'POST'])
def verify():
    form = VerifyForm()
    if 'username' in session:
        # TODO: Add stuff from database
        return render_template("verify.html", page_title="Add Products", name=session['username'])
    else:
        flash("Please login.")
        return redirect(url_for('auth.login'))
