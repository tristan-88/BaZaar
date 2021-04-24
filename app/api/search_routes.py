from flask import Blueprint
# we will need to import our products model and store model if we want to search stores as well
# from app.models import Product, Store
from app.forms import SearchForm
from app.models import User

search_routes = Blueprint('search', __name__)


# @search_routes.route('')
# def search():
#     # return 'INSIDE ROUTE'
#     form = SearchForm()
#     return form['search']
#     # if form.is_submitted():
#     # # searchValue = form['input'] OR form.search?
#     #     queryProduct = User.query.filter(User.username.like(searchValue))
#     # # if queryProduct:
#     #     return queryProduct
#     # #     #render the new page here
#     # # elif:
#     # #     queryStore = Store.query.filter(Store.name.like(searchValue))
#     # #     #render the new page here
