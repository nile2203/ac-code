from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    current_path = os.path.dirname(os.path.abspath(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/user.db'.format(current_path)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db, render_as_batch=True)

    from flask_jwt_extended import JWTManager
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    jwt = JWTManager(app)

    from app import models
    from app_jwt.user.views import user
    app.register_blueprint(user, url_prefix='/v1/user')

    return app
