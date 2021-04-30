from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import db, User, Product, Store


store_routes = Blueprint('stores', __name__)


@store_routes.route('/')
def get_stores():
    stores = Store.query.all()
    return {"stores": [store.to_dict() for store in stores]}


@store_routes.route('/<int:id>')
def get_store(id):
    store = Store.query.get(id)
    return [store.to_dict()]

@store_routes.route('/mystore')
def getting_store():
    store = Store.query.filter_by(user_id = current_user.id).first()
    if store:
        return store.to_dict()
    return None

@store_routes.route('/<int:id>/products')
def get_products(id):
    products = Product.query.filter_by(store_id=id).all()
    return {"products": [product.to_dict() for product in products]}
