import os

from flask import Flask


def create_app():
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import user
    app.register_blueprint(user.bp)


    return app