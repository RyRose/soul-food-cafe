from flask import Flask, Blueprint, flash, abort, session, render_template, redirect, request, url_for
from app import db
from app.forms import LoginForm, RegisterForm
from app.forms import flash_errors
from app.models import Donor, Admin

from flask.ext.testing import TestCase
import unittest

class TestLoginForm:
    username = '<input id="username" name="username" type="text" value="">'
    password = '<input id="password" name="password" type="password" value="">'
    csrf_token = '<input id="csrf_token" name="csrf_token" type="hidden" value="1462507220##914d67c8afa1aa9082368c5782bce0dd912b1913">'

class TestRegisterForm:
    email = '<input id="email" name="email" type="text" value="">'
    username = '<input id="username" name="username" type="text" value="">'
    password = '<input id="password" name="password" type="password" value="">'
    comformpassword = '<input id="password" name="password" type="password" value="">'
    csrf_token = '<input id="csrf_token" name="csrf_token" type="hidden" value="1462509784##6defc4766593160d1349da7101de6327ef85d6b2">'

class htmlTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config["TESTING"] = True
        return app

    def test_login_template(self):
        form = TestLoginForm()
        s = open("test_login.html")
        f = s.read()
        s.close()
        self.assertEqual(render_template("login.html", page_title="Login", form=form), f)

    def test_register_template(self):
        form = TestRegisterForm()
        s = open("test_register.html")
        f = s.read()
        s.close()
        self.assertEqual(render_template("register.html", page_title="Register", form=form),f)




if __name__ == '__main__':
    unittest.main()
