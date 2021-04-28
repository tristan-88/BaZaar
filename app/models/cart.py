from .db import db
from sqlalchemy import Date, DateTime
import datetime


class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    order_id = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "order_id": self.order_id,
            "products": [product.to_dict() for product in self.products]
        }

    users = db.relationship("User", back_populates="carts", cascade="all, delete")
    orders = db.relationship("Order", back_populates="carts", cascade="all, delete")
    products = db.relationship("Cart_Product", back_populates="carts")
