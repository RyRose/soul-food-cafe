from flask import Blueprint, flash, abort, session, render_template, redirect, request, url_for
from app import db
from app.forms import LoginForm, RegisterForm
from app.forms import flash_errors
from app.models import Donor, Admin
from app.views import auth
import os
import unittest
import tempfile

class authTestCase(unittest.TestCase):

    def test_login(self):
        email = "none@gmail.com"
        username = "shuhao"
        password = "zsrzsr"
        donor = Donor(email,username, password)

        form = LoginForm()
        print(form)
if __name__ == '__main__':
    unittest.main()
