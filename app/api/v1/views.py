from flask_restful import Api, Resource

from . import v1_blueprint
from .endpoints import admin_endpoints, admin_and_store_attendant_endpoints

API = Api(v1_blueprint)

API.add_resource(admin_endpoints.Admin, '/products')
API.add_resource(admin_and_store_attendant_endpoints.AdminAndStoreAttendant, '/products')
API.add_resource(admin_and_store_attendant_endpoints.GetSpecificProduct, '/products/<int:product_id>')