from flask import Blueprint, jsonify, request
from flask_login import current_user
from app.models import db, Product, Store, User, Order, Cart, cart_product

cart_routes = Blueprint('carts', __name__)

# ---POST--- http://localhost:/5000 api/carts
# @cart_routes.route('/', methods=["POST"])
# def create_cart():
#     #form = CartForm()
#     if form.validate_on_submit():
#         cart = Cart(
#             user_id=current_user.id,
#             created_at=  # ,
#             upated_at=  # ,
#             order_id=  # some query here
#         )
#         db.session.add(cart)
#         db.session.commit()
#     return jsonify({'cart': cart.to_dict()} if cart else 'Error fetching cart')

#

# ---GET--- http://localhost:5000/api/carts/:id


@cart_routes.route('/<int:id>')
def single_cart(id):
    # Getting the cart so we have the userId, createdAt, updatedAt, and empty order_id
    cart = Cart.query.get(id)
    # get the cartProducts id's so we have the products associated with their cart
    # cartProducts = Session.query(cart_product).filter(cart_product.c.cart_id==id).all()
    # return jsonify({'cart': cart.to_dict()})
    return jsonify(cart.to_dict())

# ---PATCH--- http://localhost:5000/api/carts/:id


@cart_routes.route('/<int:id>', methods=["PATCH"])
def edit_cart(id):
    cart = Cart.get(id)
    # too tired to think
    cart = Cart.query.get(id)
    if cart:
        content = request.json['content']
        cart.content = content
        db.session.commit()
    return jsonify(cart.to_dict() if cart else 'Failed to update users cart')

# ---DELETE --- http://localhost:5000/api/cart/:id


@cart_routes.route('/<int:id>', methods=["Post"])
def delete_cart(id):
    remove_cart = Cart.query.filter(Cart.id == id).delete()
    db.session.commit()
    return jsonify('Cart was succefully deleted!' if remove_cart else "Could not delete cart")
