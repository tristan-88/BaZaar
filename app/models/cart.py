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
            "order_id": self.order_id
        }

    cart_user = db.relationship("User", back_populates="user_cart", cascade="all, delete")
    cart_order = db.relationship("Order", back_populates="order_cart", cascade="all, delete")
    cart_cartProduct = db.relationship("Cart_Product", back_populates="cartProduct_cart")
