import uuid

from flask import Blueprint, current_app as app, render_template, redirect, url_for, session, request
from core.db.mongo_manager import DBManager
from core.revolver import Revolver
from flask_security import login_required

import logging
logger = logging.getLogger('root')

bp = Blueprint('api', __name__, url_prefix="/api")


@bp.route("/new_revolver", methods=['GET'])
def new_revolver():
    return render_template("pages/new_revolver.html")


@bp.route("/add_revolver", methods=['POST'])
def add_revolver():
    try:
        r = Revolver(request.form.get('new_name'),
                                             request.form.get('new_descr'),
                                             int(request.form.get('new_drum_capacity')),
                                             float(request.form.get('new_drum_turn_period')))
        DBManager().add_revolver(r)
        logging.info(f"Revolver added: {r}")
        return redirect(url_for('stats.revolvers'))
    except Exception as e:
        logging.exception(e)
        return f"Error occured. Contact server administration.", 200
