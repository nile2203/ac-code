from flask import Blueprint

employee = Blueprint('employee', __name__)

from app.employee.views import *