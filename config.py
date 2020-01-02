import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-top-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlurl'
    SQLALCHEMY_TRACK_MODIFICATIONS = False