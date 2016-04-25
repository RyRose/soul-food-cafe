import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = b'\x90\xef\xf4\x0f\x19P\xf9\xaa\x84D\t\x84\xdc\x19K\x87\xbe\xddZQ\x15\x1654'
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASEDIR, 'app.db')
