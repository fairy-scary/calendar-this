from flask import Blueprint

bp = Blueprint('', __name__)

@bp.route("/")
def index():
    return "<h1>Hi!</h1>"