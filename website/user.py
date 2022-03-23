from flask import Blueprint, render_template

bp = Blueprint('user', __name__)


@bp.route('/')
def index():
    return render_template('user/simon.html')

@bp.route('/simon')
def index():
    return render_template('user/simon.html')

@bp.route('/trenton')
def index():
    return render_template('user/trenton.html')

@bp.route('/sean')
def index():
    return render_template('user/sean.html')

@bp.route('/jermaine')
def index():
    return render_template('user/jermaine.html')

