from flask.cli import AppGroup
from .users import seed_users, undo_users
from .stores import seed_stores, undo_stores
from .products import seed_products, undo_products
from .tags import seed_tags, undo_tags
from .reviews import seed_reviews, undo_reviews
from .product_tags import seed_product_tags, undo_product_tags
from .favorites import seed_Favorites, undo_Favorites
from .carts import seed_carts, undo_carts
from .cart_products import seed_cart_products, undo_cart_products
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command


@seed_commands.command('all')
def seed():
    # Add seed functions here
    seed_users()
    seed_stores()
    seed_products()
    seed_tags()
    seed_reviews()
    seed_Favorites()
    seed_product_tags()
    seed_carts()
    seed_cart_products()
# Creates the `flask seed undo` command


@seed_commands.command('undo')
def undo():
    # Add undo functions here
    undo_users()
    undo_stores()
    undo_products()
    undo_tags()
    undo_reviews()
    undo_Favorites()
    undo_product_tags()
    undo_carts()
    undo_cart_products()
