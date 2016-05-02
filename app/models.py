from datetime import datetime
from app import db

from werkzeug.security import generate_password_hash, \
             check_password_hash

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    username = db.Column(db.Text)
    password = db.Column(db.Integer, unique=True)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<Donor %r>' % self.username

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Integer, unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):
        return "<Admin %r>" % self.username

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey("donor.id"))
    donor = db.relationship('Donor',
                    backref=db.backref('donations'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item = db.relationship('Item',
                    backref=db.backref('donations'))
    quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, item, donor, quantity, date):
        self.item = item
        self.donor = donor
        self.quantity = quantity
        if date is None:
            date = datetime.utcnow()
        self.date = date

    def __repr__(self):
        return "<Donation %d, %d, %d, %r>" % self.donor_id, self.item_id, self.quantity, str(self.date)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.Text)
    name = db.Column(db.Text)
    weight = db.Column(db.Float)
    brand = db.Column(db.Text)

    def __init__(self, barcode, name, weight, brand):
        self.barcode = barcode
        self.name = name
        self.weight = weight
        self.brand = brand

    def __repr__(self):
        return "<Item %r, %r, %r, %r>" % self.name, self.barcode, str(self.weight), self.brand

