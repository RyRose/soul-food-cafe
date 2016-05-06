from flask import Blueprint, render_template, redirect, session, flash, url_for
from flask_table import Table, Col, DateCol
from app.forms import VerifyForm, ScanningForm, flash_errors
from app.models import Donation, Donor, Item
from flask import Flask, request, jsonify
from flask.ext import excel
from datetime import datetime
from app import db

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
def scanning():
        if 'is_admin' in session:
            form = ScanningForm()
            if form.validate_on_submit():
                donor = form.data['donor']
                barcode = form.data['barcode']
                return redirect(url_for("donation.manual", donor=donor,barcode=barcode))
            else:
                flash_errors(form)

            return render_template("add.html", page_title="Add Products", form = form, scanning=True)
        else:
            flash("Please login.")
            return redirect(url_for('auth.admin_login'))


@donation.route("/donations/add/<donor>/<barcode>", methods = ['GET', 'POST'])
def manual(donor, barcode):
    if 'is_admin' in session:
        form = VerifyForm()
        if request.method == 'GET':
            print(barcode)
            item = Item.query.filter_by(barcode=barcode).first()
            if item is not None:
                form.name.data = item.name
                form.weight.data = item.weight
                form.brand.data = item.brand
            form.donor.data = donor
            form.barcode.data = barcode
            form.date.data = datetime.now()
            return render_template("add.html", page_title="Add Products", form=form, scanning=False)

        if form.validate_on_submit():
            item = Item.query.filter_by(barcode=form.data["barcode"]).first()
            donor = Donor.query.filter_by(username=form.data["donor"]).first()
            if item is None:
                item = Item(form.data["barcode"], form.data["name"], form.data["weight"], form.data["brand"])
            donation = Donation(item, donor, form.data["quantity"], datetime.strptime(form.data['date'], "%Y-%m-%d %H:%M:%S.%f"))
            db.session.add(donation)
            db.session.commit()
            return redirect(url_for("donation.scanning"))
        else:
            flash_errors(form)
            return render_template("add.html", page_title="Add Products", form=form, scanning=False)

    else:
        flash("Please login.")
        return redirect(url_for('auth.admin_login'))

def make_donation_list(donation):       
    return [donation.item.name, donation.item.brand, donation.item.weight]

@donation.route("/download", methods=['GET'])
def download_file():
    donations = Donation.query.all()
    donations = [ make_donation_list(donation) for donation in donations]
    return excel.make_response_from_array(donations, "csv", file_name="export_data")
