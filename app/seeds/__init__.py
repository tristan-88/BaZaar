from flask.cli import AppGroup
from .users import seed_users, undo_users
from .stores import seed_stores, undo_stores
from .products import seed_products, undo_products
from .tags import seed_tags, undo_tags
from .reviews import seed_reviews, undo_reviews
from .product_tags import seed_Product_Tags, undo_Product_Tags
from .favorites import seed_Favorites, undo_Favorites
from .carts import seed_carts, undo_carts
from .cart_products import seed_Cart_Products, undo_Cart_Products
from .photos import seed_photos, undo_photos
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
    seed_Product_Tags()
    seed_carts()
    seed_Cart_Products()
    seed_photos()
# Creates the `flask seed undo` command


@seed_commands.command('undo')
def undo():
    # Add undo functions here
    undo_Product_Tags()
    undo_Cart_Products()
    undo_Favorites()
    undo_users()
    undo_stores()
    undo_products()
    undo_tags()
    undo_reviews()
    undo_carts()
    undo_photos()
