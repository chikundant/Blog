from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login.init_app(app)
login.login_view = 'login'

app.debug = True


from project import routs
