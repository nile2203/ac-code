from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    current_path = os.path.dirname(os.path.abspath(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/employee.db'.format(current_path)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    from app import models
    from app.employee.views import employee
    app.register_blueprint(employee, url_prefix='/v1/employee')

    from app.department.views import department
    app.register_blueprint(department, url_prefix='/v1/department')

    from flask_swagger_ui import get_swaggerui_blueprint
    swagger_url = '/swagger'
    api_url = '/static/swagger.json'
    swagger_ui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config={
            'app_name': 'Flask-1'
        }
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=swagger_url)

    return app
