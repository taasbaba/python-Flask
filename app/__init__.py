'''Flask application instance'''
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# flask-login initialization
from flask_login import LoginManager

app = Flask(__name__)
# Loading config
app.config.from_object(Config)
# congigure DB through sqlAlchemy
db = SQLAlchemy(app)
# prepare database migrate
migrate = Migrate(app, db)
# flask-login initialization
login = LoginManager(app)
'''
The 'login' value above is the function (or endpoint) name for the login view.
In other words, the name you would use in a url_for() call to get the URL.
'login' 表示 route 中的 login page.
'''
login.login_view = 'login'

from app import routes, models