from flask import Blueprint

v1_blueprint = Blueprint('v1_blueprint', __name__)
auth_v1_blueprint = Blueprint('auth_v1_blueprint', __name__)

from . import views