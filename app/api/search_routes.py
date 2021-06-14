from flask import Blueprint
from app.forms import SearchForm
from app.models import User, Product, Store

search_routes = Blueprint('search', __name__)

@search_routes.route('/<string:squery>')
def search(squery):

    search_result = {
        'Products': [],
        'Stores': []
    }

    product_results = Product.query.filter(Product.name.ilike(f'%{squery}%')).all()
    store_results = Store.query.filter(Store.name.ilike(f'%{squery}%')).all()

    search_result['Products'] = [product.to_dict() for product in product_results]
    search_result['Stores'] = [store.to_dict() for store in store_results]

    return search_result