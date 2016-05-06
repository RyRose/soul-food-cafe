from flask import Blueprint, render_template, redirect, session, flash, url_for
from flask_table import Table, Col, DateCol
from app.forms import VerifyForm
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
def verify():
        if 'is_admin' in session:
            form = VerifyForm()
            if form.validate_on_submit():
                # TODO: Add stuff from database
                donor = form.data['donor']
                barcode = form.data['barcode']
                redirect(url_for("donation.add/" + donor + "/" + barcode))

            return render_template("verify.html", page_title="Add Products", form = form, is_adding=False)
        else:
            flash("Please login.")
            return redirect(url_for('auth.admin_login'))


@donation.route("/donations/add/<donor>/<barcode>", methods = ['GET', 'POST'])
def manual(donor, barcode):
    if 'is_admin' in session:
        form = VerifyForm()
        if request.method == 'GET':
            item = Item.query.filter_by(barcode=barcode).first()
            if item is not None:
                form.data['donor'] = donor
                form.data['name'] = Item.name
                form.data['weight'] = Item.weight
                form.data['brand'] = Item.brand
                form.data['date'] = datetime.utcnow()
            else:
                form.data['donor'] = donor
                form.data['date'] = datetime.utcnow()
            return render_template("verify.html", page_title="Add Products", form=form, adding=True)
        if form.validate_on_submit():
            item = Item.query.filter_by(barcode=barcode).first()
            donor = Donor.query.filter_by(username=donor).first()
            if item is None:
                item = Item(barcode, form.data["name"],form.data["weight"], form.data["brand"])
            donation = Donation(item, donor, form.data["quantity"], form.data['date'])
            db.session.add(donation)
            db.session.commit()
            return redirect(url_for("donation.verify"))
        else:
            return render_template("verify.html", page_title="Add Products", form=form, adding=True)

    else:
        flash("Please login.")
        return redirect(url_for('auth.admin_login'))


@donation.route("/download", methods=['GET'])
def download_file():
    return excel.make_response_from_array([[1,2], [3, 4]], "csv")

@donation.route("/export", methods=['GET'])
def export_records():
    return excel.make_response_from_array([[1,2], [3, 4]], "csv", file_name="export_data")
