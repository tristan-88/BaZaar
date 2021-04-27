from .db import db

# Joins Tables
# favorites = db.Table(
#     "favorites",
#     db.Column("user_id", db.Integer, db.ForeignKey(
#         "users.id"), primary_key=True),
#     db.Column("product_id", db.Integer, db.ForeignKey(
#         "products.id"), primary_key=True),
# )


class Favorites(db.Model):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
        }

    favorite_user = db.relationship("User", back_populates="user_favorite")
    favorite_product = db.relationship(
        "Product", back_populates="product_favorite")


product_tag = db.Table(
    "product_tag",
    db.Column("product_id", db.Integer, db.ForeignKey(
        'products.id'), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True)
)


cart_product = db.Table(
    "cart_product",
    db.Column("product_id", db.Integer, db.ForeignKey(
        'products.id'), primary_key=True),
    db.Column("cart_id", db.Integer, db.ForeignKey(
        "carts.id"), primary_key=True)
)
