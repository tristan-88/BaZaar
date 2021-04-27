from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import db, User, Product, Store


store_routes = Blueprint('stores', __name__)


@store_routes.route('/')
def get_stores():
    stores = Store.query.all()
    return {"stores": [stores.to_dict() for store in stores]}


@store_routes.route('/<int:id>/products')
def get_products(id):
    products = Product.query.filter_by(store_id=id).all()
    return {"products": [product.to_dict() for product in products]}


@store_routes.route('/<int:id>/')
