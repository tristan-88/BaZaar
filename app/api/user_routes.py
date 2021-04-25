from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import db, User

user_routes = Blueprint('users', __name__)
# for route  testing


tests = {'Message': 'Hello'}

# http://localhost:5000/api/users


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}


# http://localhost:5000/api/users
@user_routes.route('/', methods=['POST'])
def create_user():
    return jsonify(tests)


# http://localhost:5000/api/users/:id
@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()

# ---DELETE--- http://localhost:5000/api/users/:id ---UNTESTED---


# @user_routes.route('/<int:id>', methods=['DELETE'])
# @login_required
# def delete_user(id):
#     remove_user = User.query.filter(User.id == id).delete()
#     db.session.commit()
#     return jsonify('User succefully deleted!' if remove_user else 'Could not delete user.')
