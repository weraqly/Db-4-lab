import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from my_project.auth.route import register_routes
from flasgger import Swagger

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default-secret-key")

    app.config['SWAGGER'] = {
        'title': 'My Project API',
        'uiversion': 3
    }

    Swagger(app)

    _init_db(app)
    register_routes(app)

    return app


def _init_db(app: Flask) -> None:
    db.init_app(app)

    db_uri = app.config["SQLALCHEMY_DATABASE_URI"]
    if not database_exists(db_uri):
        create_database(db_uri)

    import my_project.auth.domain
    with app.app_context():
        db.create_all()