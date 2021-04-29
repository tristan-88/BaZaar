from .db import db
from .tables import Favorites, Product_Tag


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    price = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "store_id": self.store_id,
            "price": self.price,
            "quantity": self.quantity,
            "description": self.description,
            "reviews": [review.to_dict() for review in self.reviews],
            "photos": [photo.to_dict() for photo in self.photos],
            "favorite": [favorite.to_dict() for favorite in self.favorites],
            "tag": [tag.to_dict() for tag in self.tags]
        }

    stores = db.relationship(
        "Store", back_populates="products", cascade="all, delete")
    reviews = db.relationship(
        "Review", back_populates="products", cascade="all, delete")
    photos = db.relationship(
        "Photo", back_populates="products", cascade="all, delete")
    favorites = db.relationship(
        "Favorites", back_populates="products", cascade="all, delete")
    tags = db.relationship("Product_Tag", back_populates="products", cascade="all, delete")
    carts = db.relationship("Cart_Product", back_populates="products", cascade="all, delete")

