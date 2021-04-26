from .db import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    price = db.Column(db.Numeric(6, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2000), nullable=False)

    product_store = db.relationship(
        "Store", back_populates="store_product")
    product_review = db.relationship("Review", back_populates="review_product")
    product_user = db.relationship(
        "User", secondary=favorites, back_populates="user_product")
