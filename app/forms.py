from wtforms import BooleanField, TextField, PasswordField, validators
from flask_wtf import Form

class LoginForm(Form):
    username = TextField('Username', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])

class RegisterForm(Form):
    email = TextField('Email Address', [validators.Email(message = "Please enter a valid email")])
    username = TextField('Username', [validators.InputRequired()])
    password = PasswordField('New Password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match') ]
        )
    confirm = PasswordField('Repeat Password')