from flask import flash

from wtforms import BooleanField, TextField, PasswordField, validators
from flask_wtf import Form

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

class LoginForm(Form):
    username = TextField('Username', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])

class RegisterForm(Form):
    email = TextField('Email Address', [validators.InputRequired(), validators.Email(message = "Please enter a valid email")])
    username = TextField('Username', [validators.InputRequired()])
    password = PasswordField('Password', [
        validators.InputRequired(),
        validators.EqualTo('confirm_password', message='Passwords must match') ]
        )
    confirm_password = PasswordField('Confirm Password')
    
class VerifyForm(Form):
    name = TextField('Name', [validators.InputRequired()])
    brand = TextField('Brand', [validators.InputRequired()])
    weight = TextField('Weight', [validators.InputRequired()])
    quantity = TextField('Quantity', [validators.InputRequired()])
    date = TextField('Date', [validators.InputRequired()])
