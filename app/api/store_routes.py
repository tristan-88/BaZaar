from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Product, Store
from app.forms import ShopForm
from app.awsupload import (
    upload_file_to_s3, allowed_file, get_unique_filename)


store_routes = Blueprint('stores', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


@store_routes.route('/')
def get_stores():
    stores = Store.query.all()
    return {"stores": [store.to_dict() for store in stores]}


@store_routes.route('/<int:id>')
def get_store(id):
    store = Store.query.get(id)
    return store.to_dict()

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


@store_routes.route('/mystore', methods=['POST'])
def create_post():
    """
    Creates a new shop for a user that is logged in
    """
    if "image" not in request.files:
        return {"errors": "image required"}, 400

    image = request.files["image"]

    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)

    upload = upload_file_to_s3(image)

    if "url" not in upload:

        return upload, 400

    url = upload["url"]


    form = ShopForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        shop = Store(
            name=form.data["name"],
            address=form.data["address"],
            user_id=current_user.id,
            description=form.data["description"],
            photo_url=url
        )
        db.session.add(shop)
        db.session.commit()
        return shop.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
