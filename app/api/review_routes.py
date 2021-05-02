from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from app.models import db, Product, Store, Review, Photo, User
from app.forms import ReviewForm
from sqlalchemy import desc, asc

review_routes = Blueprint('reviews', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


@review_routes.route('/')
def get_reviews():
    reviews = Review.query.all()
    return {"review": [review.to_dict() for review in reviews]}

@review_routes.route('/<int:id>')
def get_review(id):
    review = Review.query.get(id)
    return review.to_dict()

@review_routes.route('/myreviews/<int:id>/')
def gets_reviews(id):
    reviews = Review.query.filter_by(user_id = id).all()
    if len(reviews):
        return {'user_reviews': [review.to_dict() for review in reviews]}
    return {'message': 'This user has review'}

@review_routes.route('/<int:id>/products')
def getting_reviews(id):
    reviews = Review.query.filter_by(product_id = id).all()
    if len(reviews):
        return {'product_reviews':[review.to_dict() for review in reviews]}
    return {'message': 'There are no reviews for this product'}

@review_routes.route('/myreviews/<int:id>', methods=['POST'])
def create_review():
    '''
    CREATES A NEW REVIEW
    '''
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review = Review(
            user_id= id
            # content = form.data['Review']
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return None