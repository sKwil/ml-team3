from flask import Blueprint, render_template

bp = Blueprint('user', __name__)


@bp.route('/')
def index():
    return render_template('website-layout/base2.html')


@bp.route('/simon')
def simon_index():
    return render_template('website-layout/simon.html')


@bp.route('/trenton')
def trenton_index():
    return render_template('website-layout/trenton.html')


@bp.route('/sean')
def sean_index():
    return render_template('website-layout/sean.html')


@bp.route('/jermaine')
def jermaine_index():
    return render_template('website-layout/jermaine.html')

@bp.route('/weather')
def weather_index():
    return render_template('website-layout/weather.html')

