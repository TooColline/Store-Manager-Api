from flask_restful import Api, Resource

from . import v1_blueprint, auth_v1_blueprint
from .endpoints import admin_endpoints, admin_and_store_attendant_endpoints, store_attendant_endpoint, authorization

API = Api(v1_blueprint)
API_AUTH = Api(auth_v1_blueprint)

API.add_resource(admin_endpoints.AddProduct, '/products')
API.add_resource(admin_and_store_attendant_endpoints.GetAllProducts, '/products')
API.add_resource(admin_and_store_attendant_endpoints.GetSpecificProduct, '/products/<int:product_id>')
API.add_resource(store_attendant_endpoint.AddSale, '/saleorder')
API.add_resource(admin_endpoints.GetAllSales, '/saleorder')
API.add_resource(store_attendant_endpoint.SpecificSaleRecord, '/saleorder/<int:sale_id>')

API_AUTH.add_resource(authorization.SignUp, '/signup')
API_AUTH.add_resource(authorization.Login, '/login')
