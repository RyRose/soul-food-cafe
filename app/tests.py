from app import models
import os
import unittest
import tempfile
from app.views import donations
from app import db
from app.models import Donation, Donor, Admin, Item

class modelsTestCase(unittest.TestCase):

    def test_Donor_check_password(self):
        email = "shuhaokou@gmail.com"
        username = "user"
        password = "pass"
        donor = Donor(email,username, password)
        self.assertTrue(donor.check_password(password))

    def test_Donor_init(self):
        email = "shuhaokou@gmail.com"
        username = "user"
        password = "pass"
        donor = Donor(email,username, password)
        self.assertEqual(donor.email,"shuhaokou@gmail.com")
        self.assertEqual(donor.username, "user")
        self.assertTrue(donor.check_password(password))

    def test_Donor_repr(self):
        email = "shuhaokou@gmail.com"
        username = "user"
        password = "pass"
        donor = Donor(email,username, password)
        self.assertEqual(donor.__repr__(), "<Donor None: user, shuhaokou@gmail.com>")

    def test_Admin_init(self):
        username = "user"
        password = "pass"
        admin = Admin(username, password)
        self.assertEqual(admin.username, "user")
        self.assertTrue(admin.check_password(password))

    def test_Admin_repr(self):
        username = "user"
        password = "pass"
        admin = Admin(username, password)
        self.assertEqual(admin.__repr__(), "<Admin None: user>")

    def test_Admin_check_password(self):
        username = "user"
        password = "pass"
        admin = Admin(username, password)
        self.assertTrue(admin.check_password(password))

    def test_Item_init(self):
        barcode = "123123123"
        name = "coke"
        weight = "50"
        brand = "cocacola"
        item = Item(barcode, name, weight, brand)
        self.assertEqual(item.barcode, "123123123")
        self.assertEqual(item.name, "coke")
        self.assertEqual(item.weight, "50")
        self.assertEqual(item.brand, "cocacola")

    def test_Item_repr(self):
        barcode = "123123123"
        name = "coke"
        weight = "50"
        brand = "cocacola"
        item = Item(barcode, name, weight, brand)
        self.assertEqual(item.__repr__(), "<Item None: coke, " +
        "123123123, 50, cocacola>")

    def test_Donation_init_and_repr(self):
        email = "shuhaokou@gmail.com"
        username = "donor"
        password = "donorupass"
        donor = Donor(email,username, password)

        username = "admin"
        password = "adminpass"
        admin = Admin(username, password)

        barcode = "123123123"
        name = "coke"
        weight = "50"
        brand = "cocacola"
        item = Item(barcode, name, weight, brand)

        quantity = "10"
        date = "Jan"

        donation = Donation(item, donor, quantity, date)

        self.assertEqual(item.__repr__(), "<Item None: coke, 123123123, 50, cocacola>")
        self.assertEqual(donor.__repr__(), "<Donor None: donor, shuhaokou@gmail.com>")
        self.assertEqual(quantity, "10")
        self.assertEqual(date, "Jan")

        self.assertEqual(donation.__repr__(), "<Donation None: 10, Jan, "+
        "<Item None: coke, 123123123, 50, cocacola>, <Donor None: donor, "+
        "shuhaokou@gmail.com>>")



    print("1,2,3,4,5,!!!!!!!!!!!!!!!!!!!!!!")

if __name__ == '__main__':
    unittest.main()
