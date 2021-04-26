from .db import db
from .tables import favorites, product_tag, product_photo


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    price = db.Column(db.Numeric(6, 2), nullable=False)
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
        "Store", back_populates="store_product")
    product_review = db.relationship("Review", back_populates="review_product")
    product_user = db.relationship(
        "User", secondary=favorites, back_populates="user_product")
    product_tag = db.relationship(
        "Tag", secondary=product_tag, back_populates="tag_product")
    product_photo = db.relationship(
        "Photo", back_populates="photo_product", secondary=product_photo)
