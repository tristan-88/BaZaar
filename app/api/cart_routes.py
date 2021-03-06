from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from app.models import db, Product, Store, User, Order, Cart, Cart_Product
from sqlalchemy import desc
import datetime

cart_routes = Blueprint('carts', __name__)

# ---POST--- http://localhost:/5000 api/carts


def check_create_cart(id):
    carts = Cart.query.order_by(desc(Cart.created_at)).filter_by(user_id=id)
    # check if the cart exsists
    user_carts = [cart.to_dict() for cart in carts]
    try:
        cart = user_carts[0]
        if cart["order_id"] is None:
            return jsonify(cart)
    except:
        print('hi')
    new_cart = Cart(user_id=id)
    db.session.add(new_cart)
    db.session.commit()
    return new_cart.to_dict()


@cart_routes.route('', methods=["GET", "POST"])
# @login_required
def assign_cart():
    return check_create_cart(current_user.id)


# ---GET--- http://localhost:5000/api/carts/:id

# @cart_routes.route('/<int:id>')
# def single_cart(id):
    # Getting the cart so we have the userId, createdAt, updatedAt, and empty order_id
    # cart = Cart.query.get(id)
    # get the cartProducts id's so we have the products associated with their cart
    # cartProducts = Session.query(cart_product).filter(cart_product.c.cart_id==id).all()
    # return jsonify({'cart': cart.to_dict()})
    # return jsonify(cart.to_dict())

# ---PATCH--- http://localhost:5000/api/carts/:id


# @cart_routes.route('/<int:id>', methods=["PATCH"])
# def edit_cart(id):
#     cart = Cart.get(id)
#     # too tired to think/ grabbing cart by id
#     cart = Cart.query.get(id)
#     if cart:
#         content = request.json['content']
#         cart.content = content
#         db.session.commit()
#     return jsonify(cart.to_dict() if cart else 'Failed to update users cart')

# ---DELETE --- http://localhost:5000/api/cart/:id


@cart_routes.route('/<int:id>', methods=["POST"])
def delete_cart(id):
    remove_cart = Cart.query.filter(Cart.id == id).delete()
    db.session.commit()
    return jsonify('Cart was succefully deleted!' if remove_cart else "Could not delete cart")


# add a product
@cart_routes.route('/<int:cart_id>/add/<int:product_id>', methods=['POST', "PUT"])
@login_required
def add_item(cart_id, product_id):
    cur_entry = Cart_Product.query.filter_by(cart_id=cart_id, product_id=product_id).first()
    if not cur_entry == None:
        cur_entry.quantity += 1
        db.session.add(cur_entry)        
        db.session.commit()
        return cur_entry.to_dict()
    else:
        new_entry = Cart_Product(
            product_id=product_id,
            cart_id=cart_id,
            quantity=1
        )
        db.session.add(new_entry)        
        db.session.commit()
        return new_entry.to_dict()
        


@cart_routes.route('/<int:cart_id>/remove/<int:product_id>')
@login_required
def remove_item(cart_id, product_id):
    try:
        remove_entry = Cart_Product.query.order_by(desc(Cart_Product.id)).filter_by(
            cart_id=cart_id, product_id=product_id).first()
        db.session.delete(remove_entry)
        db.session.commit()
        return {"result": "this item"}
    except:
        return {"result": "nah this does not work"}

#Decrement route
@cart_routes.route('/<int:cart_id>/remove/<int:product_id>', methods=["PUT"])
@login_required
def decrement_item(cart_id, product_id):
    try:
        remove_entry = Cart_Product.query.order_by(desc(Cart_Product.id)).filter_by(
            cart_id=cart_id, product_id=product_id).first()
        remove_entry.quantity -= 1
        if remove_entry.quantity == 0:
            db.session.delete(remove_entry)
        db.session.commit()
        return {"result": "item count decremented"}
    except:
        return {"result": "nah this does not work"}
    #cannot just return a string!!!


@cart_routes.route('/<int:cart_id>/close/')
@login_required
def close_cart(cart_id):
    cart = Cart.query.get(cart_id)
    order = Order(
        user_id=current_user.id,
        cart_id=cart_it
    )

    cart_items = Cart_Listing.query.filter_by(cart_id=cart_id).all()

    cart.order_id = order_id
    db.session.commit()
    return cart.to_dict()

    # grab cart by id, create new order, give it user id and cart it, cart order =
