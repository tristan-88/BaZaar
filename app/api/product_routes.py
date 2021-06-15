from flask import Blueprint, jsonify, request
from flask_login import current_user
from app.models import db, Product, Store, Review, Photo, Cart_Product, Product_Tag
from app.forms import ProductForm
from sqlalchemy import desc, asc

product_routes = Blueprint('products', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages
# for route testing
tests = {'Message': 'Hello'}

# ---GET--- http://localhost:5000/api/products/ ---TESTED---


@product_routes.route('')
def all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

#Using Association routes
# @product_routes.route('/joshy')
# def all_something():
#     products = Product.query.get(1)
#     return products.to_dict()

# @product_routes.route('/')
# def all_something():
#     products = Product.query.get(1)
#     return {"message":products.reviews[0].users.username}


@product_routes.route('/bytag/<int:id>')
def products_by_tag(id):
    return jsonify([product.get_product() for product in Product_Tag.query.filter_by(tag_id=id).all()])


@product_routes.route('/fromcart/<int:id>')
# @login_protected
def cart_products(id):
    carts = Cart_Product.query.filter(cart_id=cart_id)
    products = [cart.to_dict() for cart in carts]
    return jsonify(products)


@product_routes.route('/<int:id>')
def single_product(id):
    product = Product.query.get(id)
    return product.to_dict()



@product_routes.route('/top5')
def top_five():
    feature_products = Product.query.all()
    product_list = [product.to_dict() for product in feature_products]
    sorted_list = sorted(product_list, key= lambda i: len(i["favorite"]), reverse=True)
    return jsonify(sorted_list[0:5])


@product_routes.route('/<int:id>/photos')
def product_photos(id):
    photos = Photo.query.filter_by(product_id=id).all()
    product_photos = {"product_photos": [photo.to_dict() for photo in photos]}
    return product_photos


# ---GET--- http://localhost:5000/api/products/id/reviews ---TESTED---
@product_routes.route('/<int:id>/reviews')
def product_reviews(id):
    reviews = Review.query.filter_by(product_id=id).all()
    return {"reviews": [review.to_dict() for review in reviews]}



# ---POST--- http://localhost:5000/api/products ---UNTESTED---


@product_routes.route('', methods=['POST'])
def create_product():
    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        product = Product(
            name=form.data["name"],
            store_id=form.data["store_id"],
            price=form.data["price"],
            quantity=form.data["quantity"],
            description=form.data["description"]
        )
        db.session.add(product)
        db.session.commit()
        # products = Product.query.order_by(desc(product_id)).all()
        # newProduct = products[-1]
        return product.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# ---PATCH--- http://localhost:5000/api/products/id ---UNTESTED---


# @product_routes.route('/<int:id>', methods=['PATCH'])
# def edit_product(id):
#     product = Product.query.get(id)

#     new_product = Product()
#     form_data = ProductForm()
#     if form_data.validate_on_submit():
#         form_data.populate_obj(new_product)
#         product = new_product
#         db.session.commit()

# ---DELETE --- http://localhost:5000/api/products/id ---untested---
@product_routes.route('/<int:id>', methods=["Delete"])
def delete_product(id):
    remove_product = Product.query.filter(Product.id == id).delete()
    db.session.commit()
    return jsonify('Product was successfully deleted!' if remove_product else "Could not delete product")
