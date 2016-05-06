from flask import Blueprint, render_template, redirect, session, flash, url_for
from flask_table import Table, Col, DateCol
from app.forms import VerifyForm
from app.models import Donation, Donor
from flask import Flask, request, jsonify
from flask.ext import excel

donation = Blueprint('donation', __name__)

class DonationTable(Table):
    classes = ['cell-border', 'donation_table']
    name = Col('Name')
    weight = Col('Weight')
    brand = Col('Brand')
    quantity = Col('Quantity')
    date = DateCol('Date')

class AdminDonationTable(Table):
    classes = ['cell-border', 'donation_table']
    donor = Col('Donor')
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

class AdminDonationRow(DonationRow):
    def __init__(self, donation):
        super().__init__(donation)
        self.donor = donation.donor.username

@donation.route("/donations")
def donations():
    if 'is_admin' in session:
        donations = Donation.query.all()
        donations = [AdminDonationRow(donation) for donation in donations]
        table = AdminDonationTable(donations)
        return render_template("donations.html", page_title="Donations", name=session['username'], table=table, admin=True)
    elif 'username' in session:
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
    if 'is_admin' in session:
        # TODO: Add stuff from database

        return render_template("verify.html", page_title="Add Products", name=session['username'])
    else:
        flash("Please login.")
        return redirect(url_for('auth.admin_login'))

"new"

def make_donation_list(donation):
    return [donation.item.name, donation.item.brand, donation.item.weight]

@donation.route("/download", methods=['GET'])
def download_file():
    donations = Donation.query.all()
    donations = [ make_donation_list(donation) for donation in donations]
    return excel.make_response_from_array(donations, "csv", file_name="export_data")
