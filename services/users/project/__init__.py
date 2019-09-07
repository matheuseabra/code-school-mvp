import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
toolbar = DebugToolbarExtension()


def create_app():

    app = Flask(__name__)
    app.debug = True

    app_settings = os.getenv('APP_SETTINGS')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config.from_object(app_settings)

    db.init_app(app)
    toolbar.init_app(app)
    

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
