from datetime import datetime
from app import db

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    password = db.Column(db.Text, unique=True)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Donor %r>' % self.email

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text, unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<Admin %r>" % self.username

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
        return "<Donation %d, %d, %d, %r>" % self.donor_id, self.item_id, self.quantity, self.date

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
        return "<Item %r, %r, %r, %r>" % self.barcode, self.name, self.weight, self.brand
