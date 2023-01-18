from flask import Flask, current_app
from flask_mongoengine import MongoEngine

from core.config import WebAppConfig as c
import os, json

from core.logging.log_settings import logging_init
from core.db.mongo_manager import DBManager
from core.revolver import Revolver

from web.index import bp as index_bp
from web.stats import bp as stats_bp
from web.api import bp as api_bp

import logging
logging = logging.getLogger('root')


def db_init():
    r = Revolver()
    DBManager().add_revolver(r)


def register_blueprints(app):
    """register routes in the app"""
    app.register_blueprint(stats_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(index_bp)


def create_app(conf):
    """init basic flask_app settings"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = conf.SECRET_KEY
    app.config['SECURITY_PASSWORD_SALT'] = conf.SECURITY_PASSWORD_SALT
    app.config['MONGODB_SETTINGS'] = conf.MONGODB_SETTINGS
    app.template_folder = conf.TEMPLATE_FOLDER
    app.static_folder = conf.STATIC_FOLDER
    return app


# logging settings init -- level, redirecting logs to mongo
logging_init()

db_init()

app = create_app(c)

register_blueprints(app)

app.run(c.IP, c.PORT)
