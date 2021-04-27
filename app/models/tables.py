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


class Product_Tag(db.Model):
    __tablename__ = "product_tags"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)

    def to_dict(self):
         return {
            "id": self.id,
            "product_id": self.product_id,
            "tag_id": self.tag_id,
        }

    productTag_tag = db.relationship("Tag", back_populates="tag_productTag")
    productTag_product = db.relationship("Product", back_populates="product_productTag")


class Cart_Product(db.Model):
    __tablename__ = "cart_products"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    cart_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "cart_id": self.cart_id,
        }

    cartProduct_cart = db.relationship("Cart", back_populates="cart_cartProduct")
    cartProduct_product = db.relationship("Product", back_populates="product_cartProduct")
