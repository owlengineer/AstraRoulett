from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_required
from core.db.mongo_manager import DBManager
from core.revolver import Revolver

import logging
logger = logging.getLogger('root')

bp = Blueprint('index', __name__)


@bp.route("/", methods=['GET'])
def index():
    return render_template("pages/index.html")


@bp.route("/session", methods=['GET'])
def session():
    try:
        db = DBManager()
        args = request.args.to_dict()
        r = db.get_revolver(args['revolver_name'])
        logger.info(f"Revs: {list(db.get_all_revolvers())}")
        revolver = Revolver(r._id, r.descr, r.drum_capacity)
        revolver.reload_drum(int(args['bullets_count']))

        db.add_player(id=args['name1'])
        db.add_player(id=args['name2'])

        res = True
        history = []
        i = 1
        while 1:
            shot = revolver.shot()
            step = [i,
                    args['name1'] if res else args['name2'],
                    revolver.barrel_bullet_index
            ]
            history.append(step)
            if shot:
                break
            res = not res
            i += 1
        if res:
            db.inc_player_wins(id=args['name2'])
            db.inc_player_deaths(id=args['name1'])
        else:
            db.inc_player_wins(id=args['name1'])
            db.inc_player_deaths(id=args['name2'])
        return render_template('pages/session.html',
                               drum_load=revolver.drum_load,
                               history=history,
                               winner=args['name2'] if res else args['name1'])

    except Exception as e:
        logger.error(f"params not decoded msg:{e}, args: {str(request.args.to_dict())}")
        return f"Error during parsing request parameters.", 403
