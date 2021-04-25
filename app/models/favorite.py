from .db import db


# class Favorite(db.Model):
#     __tablename__ = "favorites"

#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#   #  created_at = db.Column(Date)


favorites = db.Table(
    "favorites",
    db.Column("user_id", db.Integer, db.ForeignKey(
        "users.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey(
        "products.id"), primary_key=True),
)
