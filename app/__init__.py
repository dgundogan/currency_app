from flask import Blueprint
from flask_restful import Api
from app.resources.Currency import CurrencyResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(CurrencyResource, '/currencies')
