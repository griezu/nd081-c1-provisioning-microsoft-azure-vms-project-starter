"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
LOG_FILENAME = '/home/LogFiles/errores.log'
logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILENAME,encoding='utf-8', mode='a+')],format="%(asctime)s %(name)s:%(levelname)s:%(message)s",  datefmt= "%F %A %T" , level=logging.INFO)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
