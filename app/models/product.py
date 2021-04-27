from .db import db
from .tables import Favorites, product_tag


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    price = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2000), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "store_id": self.store_id,
            "price": self.price,
            "quantity": self.quantity,
            "description": self.description
        }

    product_store = db.relationship(
        "Store", back_populates="store_product", cascade="all, delete")
    product_review = db.relationship(
        "Review", back_populates="review_product", cascade="all, delete")
    product_tag = db.relationship(
        "Tag", secondary=product_tag, back_populates="tag_product", cascade="all, delete")
    product_photo = db.relationship(
        "Photo", back_populates="photo_product", cascade="all, delete")
    product_favorite = db.relationship(
        "Favorites", back_populates="favorite_product", cascade="all, delete")
