from flask import Blueprint

department = Blueprint('department', __name__)

from app.department.views import *