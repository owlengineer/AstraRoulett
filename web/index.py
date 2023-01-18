from flask import Blueprint, render_template
from flask_security import login_required

import logging
logger = logging.getLogger('root')

bp = Blueprint('index', __name__)


@bp.route("/", methods=['GET'])
def index():

    return render_template("pages/index.html")

