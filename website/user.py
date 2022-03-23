from flask import Blueprint, render_template

bp = Blueprint('user', __name__)


@bp.route('/')
def index():
    return render_template('user/simon.html')
