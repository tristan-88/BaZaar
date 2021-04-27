from flask import Blueprint, jsonify, request, redirect
from flask_login import login_required, login_user, current_user
from app.models import db, User, Product, favorites
from app.forms import SignUpForm

user_routes = Blueprint('users', __name__)
# for route  testing


tests = {'Message': 'Hello'}

# http://localhost:5000/api/users --- WORKS

# this route will return all users
@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}


# this route will query for 1 user by id
# http://localhost:5000/api/users/:id -- WORKS
@user_routes.route('/<int:id>')
# @login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()

# ---DELETE--- http://localhost:5000/api/users/:id ---WORKS---

# this route will detele a user by their unique id
@user_routes.route('/', methods=['DELETE'])
@login_required
def del_user():
    if current_user.id == 1:
        return

    userId = current_user.id
    oldUser = User.query.get(userId)
    db.session.delete(oldUser)
    db.session.commit()

    return {'message': 'success'}


# still working on this route

# @user_routes.route('/<int:id>/favorites')
# def get_favorites(id):
#     """
#     Return a users favorite products
#     """
#     favorites = favorites.query.filter_by(user_id=id).all()
#     return favorites
