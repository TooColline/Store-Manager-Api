from flask_restful import Api, Resource

from . import v1_blueprint
from .endpoints import admin_endpoints

API = Api(v1_blueprint)

API.add_resource(admin_endpoints.Admin, '/products')