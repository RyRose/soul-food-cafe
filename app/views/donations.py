from flask import Blueprint, render_template, redirect, session, flash, url_for
from flask_table import Table, Col, DateCol
from app.forms import VerifyForm
from app.models import Donation, Donor

donation = Blueprint('donation', __name__)

class DonationTable(Table):
    classes = ['cell-border', 'donation_table']
    name = Col('Name')
    weight = Col('Weight')
    brand = Col('Brand')
    quantity = Col('Quantity')
    date = DateCol('Date')

class DonationRow(object):
    def __init__(self, donation):
        self.name = donation.item.name
        self.weight = donation.item.weight
        self.brand = donation.item.brand
        self.quantity = donation.quantity
        self.date = donation.date

@donation.route("/donations")
def donations():
    if 'username' in session:
        me = Donor.query.filter_by(username=session['username']).first()
        donations = Donation.query.filter_by(donor=me)
        donations = [DonationRow(donation) for donation in donations]

        table = DonationTable(donations)
        return render_template("donations.html", page_title="Donations", name=session['username'], table=table)
    else:
        flash("Sorry, you must first login to access your donations.")
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
