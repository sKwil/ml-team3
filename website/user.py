from flask import Blueprint, render_template

bp = Blueprint('user', __name__)


@bp.route('/')
def index():
    return render_template('user/simon.html')


@bp.route('/simon')
def simon_index():
    return render_template('user/simon.html')


@bp.route('/trenton')
def trenton_index():
    return render_template('user/trenton.html')


@bp.route('/sean')
def sean_index():
    return render_template('user/sean.html')


@bp.route('/jermaine')
def jermaine_index():
    return render_template('user/jermaine.html')
