from flask import Blueprint

user = Blueprint('user', __name__)

from app_jwt.user.views import *