from flask import request, Blueprint, abort, render_template
from flask_security import login_required
from core.db.mongo_manager import DBManager
import core.config as c

import logging
logger = logging.getLogger('root')

bp = Blueprint('stats', __name__, url_prefix="/stats")


@bp.route("/", methods=['GET'])
def index():
    logger.info(f'External status check from {request.remote_addr}')
    logs_list = DBManager().get_all_logs()
    if logs_list:
        return "Subsystems are working fine", 200
    else:
        abort(403)


@bp.route("/logs", methods=['GET'])
def logs():
    logs_list = DBManager().get_all_logs()
    return render_template("pages/admin_logs.html", logs_list=list(logs_list))


@bp.route("/revolvers", methods=['GET'])
def revolvers():
    revolvers_list = DBManager().get_all_revolvers()
    return render_template("pages/revolvers.html", revolvers_list=list(revolvers_list))


@bp.route("/players", methods=['GET'])
def players():
    players_list = DBManager().get_all_players()
    return render_template("pages/players.html", players_list=list(players_list))