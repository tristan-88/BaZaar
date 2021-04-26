from .db import db


# Joins Tables
favorites = db.Table(
    "favorites",
    db.Column("user_id", db.Integer, db.ForeignKey(
        "users.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey(
        "products.id"), primary_key=True),
)


product_tag = db.Table(
    "product_tag",
    db.Column("product_id", db.Integer, db.ForeignKey(
        'products.id'), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True)
)


# product_photo = db.Table(
#     "product_photo",
#     db.Column("product_id", db.Integer, db.ForeignKey(
#         'products.id'), primary_key=True),
#     db.Column("photo_id", db.Integer, db.ForeignKey(
#         "photos.id"), primary_key=True)
# )


cart_product = db.Table(
    "cart_product",
    db.Column("product_id", db.Integer, db.ForeignKey(
        'products.id'), primary_key=True),
    db.Column("cart_id", db.Integer, db.ForeignKey(
        "carts.id"), primary_key=True)
)
