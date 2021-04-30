from flask import Blueprint, jsonify, redirect, request
from flask_login import current_user
from app.models import db, Photo
from app.forms import PhotoForm
from app.awsupload import (
    upload_file_to_s3, allowed_file, get_unique_filename)

photo_routes = Blueprint('photos', __name__)


@photo_routes.route('', methods=["POST"])
def add_product_photos():
    """
    Adds photos for a product we create
    """
    if "image" not in request.files:
        return {"errors": "image required"}, 400

    image = request.files["image"]

    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)

    upload = upload_file_to_s3(image)

    if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when we tried to upload
        # so we send back that error message
        return upload, 400

    url = upload["url"]

    form = PhotoForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        photo = Photo(
            product_id=form.data["product_id"],
            photo_url=url
        )
        db.session.add(photo)
        db.session.commit()
        return photo.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
