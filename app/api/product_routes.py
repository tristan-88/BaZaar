from flask import Blueprint, jsonify
from flask_login import current_user
from app.models import db, Product, User

product_routes = Blueprint('products', __name__)

#for route testing
tests = {'Message':'Hello'}

#http://localhost:5000/api/products
@product_routes.route('/')
def all_products():
    return jsonify(tests)

#http://localhost:5000/api/products
@product_routes.route('/', methods=['POST'])
def create_product():
    return jsonify(tests)

#http://localhost:5000/api/products/id
@product_routes.route('/<int.id>')
def single_product(id):
   product_query = db.session.query(Product, User).join(User, User.id == current_user.id).filter(Product.id == id).first()
   return jsonify(product_query)
