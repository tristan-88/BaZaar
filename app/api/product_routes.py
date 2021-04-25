from flask import Blueprint, jsonify
from flask_login import current_user
from app.models import db, Product, User

product_routes = Blueprint('products', __name__)

#for route testing
tests = {'Message':'Hello'}

#---GET--- http://localhost:5000/api/products/ ---UNTESTED---
@product_routes.route('/')
def all_products():
    return jsonify(tests)

#---POST--- http://localhost:5000/api/products ---UNTESTED---
@product_routes.route('/', methods=['POST'])
def create_product():
    return jsonify(tests)

#---GET--- http://localhost:5000/api/products/id ---UNTESTED---
@product_routes.route('/<int.id>')
def single_product(id):
   product_query = db.session.query(Product, User).join(User, User.id == current_user.id).filter(Product.id == id).first()
   return jsonify(product_query)
