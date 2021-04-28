from flask import Blueprint, jsonify
from flask_login import current_user
from app.models import db, Product, Store, Review, Photo

product_routes = Blueprint('products', __name__)

# for route testing
tests = {'Message': 'Hello'}

# ---GET--- http://localhost:5000/api/products/ ---TESTED---


@product_routes.route('/')
def all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])


# ---GET--- http://localhost:5000/api/products/id ---TESTED---


@product_routes.route('/<int:id>')
def single_product(id):
    product = Product.query.get(id)
    return product.to_dict()


@product_routes.route('/<int:id>/photos')
def product_photos(id):
    photos = Photo.query.filter_by(product_id=id).all()
    product_photos = {"product_photos": [photo.to_dict() for photo in photos]}
    # photo_urls = [k: v for k, v in product_photos.["product_photos"].items() if k == "photo_url"]
    return product_photos
    

# ---GET--- http://localhost:5000/api/products/id/reviews ---TESTED---
@product_routes.route('/<int:id>/reviews')
def product_reviews(id):
    reviews = Review.query.filter_by(product_id=id).all()
    return {"reviews": [review.to_dict() for review in reviews]}



# ---POST--- http://localhost:5000/api/products ---UNTESTED---


@product_routes.route('/', methods=['POST'])
def create_product():
    return jsonify(tests)


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
